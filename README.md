# projectLGU website

Code for site at: http://localhost


## Getting started

Make sure a recent version of Python is installed on your system.
Open this directory in a command prompt, then:

1. Install the software:
   ```
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Go to http://localhost:8000/ in your browser, or http://localhost:8000/admin/
   to log in and get to work!

## Documentation links

* To customize the content, design, and features of the site see
  [Wagtail CRX](https://docs.coderedcorp.com/wagtail-crx/).

* For deeper customization of backend code see
  [Wagtail](http://docs.wagtail.io/) and
  [Django](https://docs.djangoproject.com/).

* For HTML template design see [Bootstrap](https://getbootstrap.com/).

---

Made with ♥ using [Wagtail](https://wagtail.io/) +
[CodeRed Extensions](https://www.coderedcorp.com/cms/)

---------------------------------------------------------
Mods by teppy:
I am planning for this app to have separate views.
CRX will be the main/default view and be used for the CMS function of the app.
There will also be the integration of a social-media-like feature that will be hosted on the same domain but will present a visuals and feels separate from the CMS.

2/28/23:
The User app is already working but needs to be re-worked. Models need further scrutiny as to what attributes will be added and/or removed.
Will also need to have a separate "base" page with a separate navbar and footer for its containerized features focused on the SocMed.
Still trying to generate more ideas and come-up with ways on how to have them implemented thru code.
