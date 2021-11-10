using System;

namespace OpenCVcsharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            OpenCvHangler cv = new OpenCvHangler();
            cv.matchTemp("Fallen5.png");
        }
    }
}
