import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class WindowCapture {
    int w = 0;
    int h = 0;
    //hwnd = None
    int cropped_x = 0;
    int cropped_y = 0;
    int offset_x = 0;
    int offset_y = 0;
    //constructor
    public WindowCapture(String winName)
    {

    }

    //UpdateScreenShot
    public Image updateScreenShot() {
        try
        {
            Rectangle screenRect = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
            BufferedImage capture = new Robot().createScreenCapture(screenRect);
            return capture;

        }
        catch(Exception e)
        {
            System.out.println("ERROR");
        }
        return null;
    }


}
