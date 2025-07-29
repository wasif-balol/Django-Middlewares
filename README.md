# ⚙️ Django Middleware In-Depth

> A Django-based demo application showcasing the lifecycle of middleware methods like  
> `process_view`, `process_exception`, and `process_template_response`.  
> It also captures and analyzes users’ operating systems and visualizes the data using **Chart.js** by overriding the Django admin `change_list` template.

---

## 🚀 Features

- 🔍 Middleware lifecycle demonstration (`process_*` methods)
- 👤 Tracks user operating systems based on request data
- 📊 Graphical representation of OS stats using **Chart.js**
- 🎛️ Customization of Django admin `change_list` view
- 💡 Great for understanding **middleware internals** and admin template overrides

---

## 🧰 Requirements

- Python: `3.5` – `3.9`
- Django (version defined in `requirements.txt`)
- Chart.js (included in static files)
- Recommended: Use a **Python virtual environment**

---

## 💻 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/wasif-balol/Django-Middlewares.git

# 2. Navigate to the project directory
cd MiddleWareInDepth

# 3. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate      # 📌 On Windows: venv\Scripts\activate

# 4. Install project dependencies
pip install -r requirements.txt

# 5. Run the Django development server
python manage.py runserver
