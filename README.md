# ZIGZAG-TUFT Marketplace

![ZIGZAG-TUFT Logo](https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png)

A handcrafted marketplace platform for ZIGZAG-TUFT, an Algerian project that creates custom handmade rugs. This web application enables customers to browse products, contact sellers, and engage in conversations about items.

## 📋 Features

- **User Authentication**: Secure login and registration system
- **Product Catalog**: Browse all available handmade rugs with detailed views
- **Category Filtering**: Products organized by categories
- **Messaging System**: Built-in conversation feature for buyers to contact sellers
- **Responsive Design**: Mobile-friendly interface that works across devices
- **Admin Dashboard**: Easy product and user management for administrators

## 🛠️ Technologies

- **Backend**: Django 5.0+
- **Frontend**: HTML5, CSS3 (pure CSS, no frameworks)
- **Database**: SQLite (default Django database)
- **Authentication**: Django built-in authentication system
- **Image Handling**: Django ImageField for product images

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Clone the repository

```bash
git clone https://github.com/yourusername/ZIGZAG-TUFT-site-web.git
cd ZIGZAG-TUFT-site-web
```

### Set up a virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Database setup

```bash
# Apply migrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## 📁 Project Structure

```
ZIGZAG-TUFT-site-web/
├── conversation/         # Messaging system app
│   ├── forms.py          # Message form
│   ├── models.py         # Conversation and message models
│   ├── views.py          # Logic for conversations
│   └── urls.py           # URL routing for conversations
├── core/                 # Core app with main site functionality
│   ├── forms.py          # Login and registration forms
│   ├── views.py          # Core view functions
│   └── urls.py           # Main URL routing
├── item/                 # Item catalog app
│   ├── models.py         # Item and category models
│   ├── views.py          # Item detail views
│   └── urls.py           # URL routing for items
├── marketplace/          # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── media/                # Uploaded product images
│   └── items_images/     # Storage for item images
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
│   ├── conversation/     # Messaging templates
│   ├── core/             # Core site templates
│   └── item/             # Item detail templates
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## 🖥️ Usage

### Admin Panel

Access the admin panel at http://127.0.0.1:8000/admin/ using your superuser credentials.

From here you can:
- Add/edit product categories
- Manage product listings
- View and manage users
- Monitor conversations

### User Functions

- **Browse Products**: View all available products on the homepage
- **Filter by Category**: Find products in specific categories
- **Product Details**: View detailed information about specific items
- **Messaging**: Contact sellers about products (requires login)
- **User Account**: Register, login, and manage your account

## 📱 Screenshots

![Homepage](https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png)
*Homepage displaying featured products*

![Product Detail](https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png)
*Detailed product view*

![Messaging](https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png)
*Conversation interface*

## 🔒 Security

- CSRF protection enabled
- User authentication required for sensitive operations
- Form validation on all inputs
- Password hashing using Django's authentication system

## 🔄 Future Enhancements

- Payment gateway integration
- User reviews and ratings
- Advanced search functionality
- Wishlist feature
- Order tracking
- Multi-language support

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

ZIGZAG TUFT - [Insert contact information]

Project Link: [https://github.com/yourusername/ZIGZAG-TUFT-site-web](https://github.com/yourusername/ZIGZAG-TUFT-site-web)

---

Made with ❤️ in Algeria
