# Odoo Product Extension: QR Code & Markup Fields for Product Templates

This is a custom Odoo 17 module that extends the `product.template` model by adding useful business fields such as supplier code, markup percentage, and an auto-generated QR code.

---

## 🔧 Features

- 🏷️ **Supplier Code**: Custom text field for supplier identification.
- 📈 **Markup**: Positive float field with validation (cannot be negative).
- 📎  **QR Code**: Automatically generated QR code based on the `supplier_code`.

These fields are visible in:
- Product **Form View**
- Product **Tree/List View**
- Product **Kanban View**

---

## 🚀 How to Run the Project

1. **Clone or Download** this repository.
2. Navigate to the root of the project and run Docker:

```bash
docker-compose up --build 
```

  - Access Odoo via:

📍 http://localhost:8069

  - Login credentials:

Email: admin@example.com

Password: admin

🛠️ Technologies Used

  - Odoo 17 (Community Edition)

  - Python 3.10

  - PostgreSQL 13 (via Docker)

  - Docker & Docker Compose

  - QR Code generation using qrcode and base64 libraries

🧪 Test Data

You can test the feature by creating or editing any product:

  - Set a Supplier Code like TEST123

  - Set a positive Markup value like 2.5

  - The QR Code will be generated based on the supplier code.

Negative Markup values are not allowed and will raise a validation error.
