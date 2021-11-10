using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Emgu.CV;


using Mat = Emgu.CV.Mat;

namespace OpenCVcsharp
{
    class OpenCvHangler
    {
        public OpenCvHangler()
        {

        }

        public bool matchTemp(String imgPath)
        {
            Mat img = CvInvoke.Imread(imgPath);
            Mat imgTest = CvInvoke.Imread("cvTestImage.png");
            Mat result = new Mat();
            CvInvoke.MatchTemplate(imgTest, result, img, Emgu.CV.CvEnum.TemplateMatchingType.Ccoeff);
            double minVal =.5, maxVal=.5, threshold = 0.5;
            Point minloc = new Point();
            Point maxloc = new Point();
            CvInvoke.MinMaxLoc(result, ref minVal, ref maxVal, ref minloc, ref maxloc);
            Console.WriteLine(maxloc.ToString());
            return true;
        }
    }
}
