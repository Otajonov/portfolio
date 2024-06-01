# Personal Resume/Portfolio Website

Welcome to my personal resume/portfolio website built with Django.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Otajonov/portfolio.git
   cd portfolio
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` to view the site.

## Contributing

Feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
