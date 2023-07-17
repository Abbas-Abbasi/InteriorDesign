# وبسایت طراحی داخلی

این یک وبسایت طراحی داخلی است که با استفاده از Python Django و کتابخانه Pillow برای پردازش تصاویر ایجاد شده است. این وبسایت بر اساس یک قالب رایگان از [free-css.com](https://www.free-css.com/) ساخته شده است که به عنوان پایه برای طراحی و طرح بندی وبسایت عمل می کند.

![طراحی داخلی](https://github.com/Abbas-Abbasi/InteriorDesign/assets/137259478/7aad36bf-d7db-48ca-a8f6-9f43ddb92d57)

 
## فناوری‌های استفاده شده

- Python Django: Django یک چارچوب وب برتر است که الگوی معماری Model-View-Controller (MVC) را دنبال می کند. این چارچوب یک مجموعه قدرتمند و انعطاف پذیر برای ایجاد برنامه‌های وب فراهم می کند.
- Pillow: کتابخانه Pillow برای پردازش تصاویر در پایتون استفاده می شود. در این پروژه از آن برای کنترل آپلود تصاویر و انجام عملیات مختلف مربوط به تصاویر استفاده می شود.
- HTML/CSS/JavaScript: این وبسایت از HTML، CSS و JavaScript برای ایجاد رابط کاربری و فعالیت‌های تعاملی استفاده می کند.

## ویژگی‌ها

- رابط کاربری کاربرپسند: وبسایت دارای یک رابط کاربری ساده و مفهومی است که به بازدیدکنندگان امکان پیمایش در میان پروژه‌های طراحی داخلی را به آسانی می دهد.
- طراحی پاسخگو: قالب استفاده شده به گونه ای طراحی شده است که قابلیت پاسخگو بودن را فراهم می کند و وبسایت را بر روی انواع دستگاه ها و اندازه های صفحه نمایش بسیار خوب نمایش می دهد.
- محتوای پویا: پشتیبانی از بک-اند ساخته شده با Django امکان تولید محتوای پویا را فراهم می کند

 و شما را قادر می سازد به راحتی پروژه‌های طراحی داخلی خود را به نمایش بگذارید.
- پردازش تصاویر: از کتابخانه Pillow برای کنترل آپلود تصاویر، تغییر اندازه و بهینه سازی تصاویر برای نمایش و انجام سایر عملیات مربوط به تصاویر استفاده می شود.
- قابلیت سفارشی‌سازی: از آنجا که وبسایت با استفاده از Django ساخته شده است، قابلیت سفارشی سازی بسیار بالا است. شما می توانید به راحتی محتوا، طرح و طراحی را به منظور نمایش پروتفولیو منحصر به فرد طراحی داخلی خود تغییر دهید.

## نصب

برای اجرای وبسایت طراحی داخلی به صورت محلی، مراحل زیر را دنبال کنید:

1. نصب Python: مطمئن شوید که Python روی سیستم شما نصب شده است. شما می توانید آن را از وبسایت رسمی Python (https://www.python.org) دانلود کرده و دستورالعمل های نصب را دنبال کنید.

2. کلون کردن مخزن: مخزن حاوی پروژه Django خود را در دستگاه محلی خود کلون کنید.

3. نصب وابستگی‌ها: به مسیر پروژه بروید و با استفاده از پیپ، وابستگی‌های مورد نیاز را نصب کنید. دستور زیر را اجرا کنید:

   ```
   pip install -r requirements.txt
   ```

4. تنظیم پایگاه داده: تنظیمات پایگاه داده را در فایل settings.py پروژه Django پیکربندی کنید. شما می توانید از SQLite برای توسعه یا هر پایگاه داده پشتیبانی شده دیگر استفاده کنید.

5. اعمال مهاجرت‌ها: با اجرای دستور زیر، مهاجرت‌های پایگاه داده را اعمال کن

ید:

   ```
   python manage.py migrate
   ```

6. اجرای سرور توسعه: با اجرای دستور زیر، سرور توسعه Django را راه‌اندازی کنید:

   ```
   python manage.py runserver
   ```

7. بررسی وبسایت: وبسایت طراحی داخلی خود را باز کنید و از آن لذت ببرید!

## قالب اصلی

این پروژه بر اساس یک قالب رایگان از [free-css.com](https://www.free-css.com/) ساخته شده است. لطفاً هنگام استفاده از قالب اصلی، شرایط مربوط به مجوز را بررسی و رعایت کنید.

## اعتبارات

- [free-css.com](https://www.free-css.com/) برای ارائه قالب اصلی استفاده شده در این پروژه.
- جامعه پایتون Django برای چارچوب وب قدرتمند.
- توسعه دهندگان کتابخانه Pillow برای قابلیت های پردازش تصاویر.
- جامعه متن باز برای ایجاد و نگهداری ابزارها و کتابخانه های استفاده شده در این پروژه.

## سلب مسئولیت

این وبسایت طراحی داخلی برای استفاده آموزشی و شخصی ساخته شده است. لطفاً هنگام استفاده از قالب اصلی، هر گونه مجوز و شرایط مربوطه را بررسی و رعایت کنید. همچنین، در صورت استقرار وبسایت در محیط تولید، توصیه می شود تدابیر امنیتی مربوطه را اعمال نمایید.
-----------------------------------------------------------------------------------------------------------------
# Interior Design Website

This is an interior design website created using Python Django and the Pillow library for image processing. The website is built upon a free template obtained from [free-css.com](https://www.free-css.com/), which serves as the foundation for the website's design and layout.

## Technologies Used

- Python Django: Django is a high-level web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a powerful and flexible toolkit for building web applications.
- Pillow: Pillow is a Python library for image processing. It is used in this project to handle image uploads and perform various image-related operations.
- HTML/CSS/JavaScript: The website utilizes HTML, CSS, and JavaScript to create the user interface and provide interactivity.

## Features

- User-friendly interface: The website features a clean and intuitive user interface, allowing visitors to navigate through the interior design projects easily.
- Responsive design: The template used as a base is designed to be responsive, ensuring that the website adapts and looks great on various devices and screen sizes.
- Dynamic content: The backend built with Django enables dynamic content generation, allowing you to easily update and showcase your interior design projects.
- Image processing: The Pillow library is used to handle image uploads, resize and optimize images for display, and perform other image-related operations.
- Customizable: Since the website is built using Django, it is highly customizable. You can easily modify the content, layout, and styling to showcase your unique interior design portfolio.

## Installation

To run the interior design website locally, follow these steps:

1. Install Python: Make sure Python is installed on your system. You can download it from the official Python website (https://www.python.org) and follow the installation instructions.

2. Clone the repository: Clone the repository containing your Django project to your local machine.

3. Install dependencies: Navigate to the project directory and install the required dependencies using pip. Run the following command:

   ```
   pip install -r requirements.txt
   ```

4. Database setup: Configure the database settings in the Django project's settings.py file. You can choose to use SQLite for development or any other supported database.

5. Apply migrations: Apply the database migrations to create the necessary tables in the database. Run the following command:

   ```
   python manage.py migrate
   ```

6. Run the development server: Start the Django development server by running the following command:

   ```
   python manage.py runserver
   ```

7. Access the website: Open a web browser and enter the URL `http://localhost:8000` to access the locally running interior design website.

## Customization

To customize the website for your own interior design projects, follow these steps:

1. Update project data: Open the Django project's code and navigate to the relevant files (views, templates) where the project data is stored. Modify the content to showcase your own interior design projects.

2. Modify templates: Customize the templates (HTML, CSS, JavaScript) to match your desired layout and design. You can modify the existing templates or create new ones as needed.

3. Add images: Replace the existing images with your own interior design project images. Ensure that the images are stored in the correct directory and update the file paths accordingly.

4. Static files: If you make any changes to the static files (CSS, JavaScript, images), collect the static files by running the following command:

   ```
   python manage.py collectstatic
   ```

5. Test and deploy: Test the customized website locally to ensure everything works as expected. Once satisfied, you can deploy the website to a web server of your choice following Django deployment guidelines.

## License

The specific license terms for the base template used in this project can be

 found on the [free-css.com](https://www.free-css.com/) website. Make sure to review and comply with the licensing requirements when using the template.

For the Django code and modifications made for this project, you can choose an appropriate open-source license or customize it as per your preferences.
 
## Credits

- [free-css.com](https://www.free-css.com/) for providing the base template used in this project.
- Python Django community for the powerful web framework.
- Pillow library developers for the image processing capabilities.
- The open-source community for creating and maintaining the tools and libraries used in this project.

## Disclaimer

This interior design website is created for educational and personal use only. Make sure to review and comply with any licensing terms associated with the base template used. Additionally, consider implementing security measures when deploying the website to a production environment.

-----------------------------------------------------------------------------------------------------------------

