using System;
using System.Threading;

class Bancomat
{
    private double balance = 5000;
    private string name;

    public void Language()
    {
        while (true)
        {
            Console.Write("Выберите язык, есть 3 языка Eng, Русский, Кыргызский: ");
            Thread.Sleep(1000);
            string lan = Console.ReadLine();
            if (lan == "Кыргызский")
            {
                Console.WriteLine("Кош келиниз!");
                Kyr();
                break;
            }
            else if (lan == "Русский")
            {
                Console.WriteLine("Добро пожаловать!");
                Rus();
                break;
            }
            else if (lan == "Eng")
            {
                Console.WriteLine("Hello");
                Eng();
                break;
            }
            else
            {
                Console.WriteLine("error");
                continue;
            }
        }
    }

    public void Kyr()
    {
        Console.Write("Ф.И.О.: ");
        name = Console.ReadLine();
        Console.WriteLine($"{balance}com каражат бар ");
        Thread.Sleep(1000);
        if (Pin1())
            Oper1();
    }

    public void Rus()
    {
        Console.Write("Ф.И.О.: ");
        name = Console.ReadLine();
        Console.WriteLine($"{balance}com баланс");
        Thread.Sleep(1000);
        if (Pin())
            Oper();
    }

    public void Eng()
    {
        Console.Write("full name: ");
        name = Console.ReadLine();
        Console.WriteLine($"{balance}com balance");
        Thread.Sleep(1000);
        if (Pin3())
            Oper2();
    }

    public bool Pin()
    {
        Console.Write("Пин код: ");
        string pin = Console.ReadLine();
        if (pin.Length == 4 && int.TryParse(pin, out _))
        {
            Console.WriteLine("Принят");
            Thread.Sleep(1000);
            return true;
        }
        else
        {
            Console.WriteLine("Попробуйте снова.");
            Thread.Sleep(1000);
            return false;
        }
    }

    public bool Pin1()
    {
        Console.Write("Пин код: ");
        string pin = Console.ReadLine();
        if (pin.Length == 4 && int.TryParse(pin, out _))
        {
            Console.WriteLine("Принят");
            Thread.Sleep(1000);
            return true;
        }
        else
        {
            Console.WriteLine("Попробуйте снова.");
            Thread.Sleep(1000);
            return false;
        }
    }

    public bool Pin3()
    {
        Console.Write("pin code: ");
        string pin = Console.ReadLine();
        if (pin.Length == 4 && int.TryParse(pin, out _))
        {
            Console.WriteLine("acсept");
            Thread.Sleep(1000);
            return true;
        }
        else
        {
            Console.WriteLine("error.");
            Thread.Sleep(1000);
            return false;
        }
    }

    public void Summ()
    {
        while (true)
        {
            double[] x = { 200, 500, 1000, balance };
            Console.WriteLine(string.Join(", ", x));
            Console.Write("Введите сумму мак.10тыс.: ");
            int number = int.Parse(Console.ReadLine());
            Thread.Sleep(1000);
            if (number > balance)
            {
                Console.WriteLine("не хватает денег");
            }
            else if (number % 100 == 0 && number % 240 != 0 && number < 10000)
            {
                Console.WriteLine("Возьмите деньги");
                Thread.Sleep(2000);
                Chek(number);
                Oper();
                break;
            }
            else
            {
                Console.WriteLine("Не удалось совершить операцию");
            }
        }
    }

    public void Oper()
    {
        while (true)
        {
            Console.Write("\nчто вы хотите сделать с деньгами (вывести или внести \nнапишите stop что бы прекратить): ");
            string x = Console.ReadLine();
            if (x == "вывести")
            {
                Summ();
                break;
            }
            else if (x == "внести")
            {
                Dep();
                break;
            }
            else if (x == "stop")
            {
                Console.WriteLine("удачи");
                break;
            }
            else
            {
                Console.WriteLine("попробуйте еще");
            }
        }
    }

    public void Dep()
    {
        Thread.Sleep(1000);
        Console.Write("введите сколько хотите внести: ");
        double x = double.Parse(Console.ReadLine());
        balance += x;
        Console.WriteLine($"ваш баланм стал {balance}");
        Oper();
        Thread.Sleep(1000);
    }

    public void Chek(int number)
    {
        while (true)
        {
            Console.Write("Нужен ли вам чек?   1) Да    2) Нет:");
            string g = Console.ReadLine();
            if (g == "Да" || g == "да")
            {
                Console.WriteLine($"{name} | Общая сумма на кар
