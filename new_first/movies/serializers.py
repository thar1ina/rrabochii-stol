from rest_framework import serializers
from .models import Movie,Review,Rating,Actor


class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)



class RecursiveSerializer(serializers.Serializer):
    """Выод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class(value, context=self.context)
        return serializer.data



class ActorListSerializer(serializers.ModelSerializer):
    '''Выод из списка актеров и режжисеров'''
    class Meta:
        model = Actor
        fields = ('id', 'name', 'image')


class ActorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описани актера и режжисера"""
    class Meta:
        model = Actor
        fileds = '__all__'



class MovieListSerializer(serializers.ModelSerializer):
    """Сиписок фильмов"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()


    class Meta:
        model = Movie
        fileds = ('id', 'title', 'tagline', 'category', 'rating_user', 'middle_star', 'poster')



class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""
    class Meta:
        model = Review
        fileds = '__all__'


class RecursiveSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        filed = ('id', 'name', 'text', 'children')


class ReviewSerializer:
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        filed = ('id', 'name', 'text', 'children')


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = ActorListSerializer(read_only=True, many=True)
    genrest = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)


    class Meta:
        model = Movie
        exclude = ('draft')



class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fileds = ('star', 'movie')

    def create(self, validated_data):
        rating, _ = Rating.objecrs.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )

        return rating








