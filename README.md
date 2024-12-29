

# Multivendor

## Live Link
```
https://multivendor-4.onrender.com/
```
  
## Run Locally

Clone the project

```bash
  git clone https://github.com/sin1ter/mUltivendor.git
```

Go to the project directory

```bash
  cd mUltivendor
```

Install dependencies

# For Windows
```bash 
   python -m venv env

   env\Scripts\activate
```

 # For macOS/Linux
 ```bash
   python3 -m venv env
   
   source env/bin/activate
   ```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```
## API Reference

####  Accounts Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **POST** | `api/accounts/login/` | To login a user |
| **POST** | `/api/accounts/register/` | To register a user |


####  Vendor Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `/api/vendor/profile/` | To retrieve vendro profile |
| **PATCH** | `/api/vendor/profile/` | To update vendor profile |
| **GET** | `api/vendor/categories/` | To retrieve list of categories |
| **PUT** | `api/vendor/categories/:id/` | To update categories |
| **PATCH** | `/api/vendor/categories/:id/` | To update a detail of a single category |
| **DELETE** | `api/vendor/categories/:id/` | To delete a single category |

| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `api/vendor/subcategories/` | To retrieve list of subcategories |
| **PUT** | `api/vendor/subcategories/:id/` | To update subcategories |
| **PATCH** | `/api/vendor/subcategories/:id/` | To update a detail of a single subcategories |
| **DELETE** | `api/vendor/subcategories/:id/` | To delete a single subcategories |

| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `api/vendor/product/` | To retrieve list of product |
| **PUT** | `api/vendor/product/:id/` | To update product |
| **PATCH** | `/api/vendor/product/:id/` | To update a detail of a single product |
| **DELETE** | `api/vendor/product/:id/` | To delete a single product |

#### Customers Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `api/customers/product/` | To retrieve list of product |
| **GET** | `api/customers/product/:id/` | To view a single product |
| **GET** | `api/customers/subcategories/` | To retrieve list of subcategories |
| **GET** | `api/customers/subcategories/:id/` | To get a singele subcategories |
| **GET** | `api/customers/subcategories/` | To retrieve list of category |
| **GET** | `api/customers/subcategories/:id/` | To get a single categories |

#### Cart Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `api/cart/` | To get all the cart items of particular user |
| **POST** | `api/cart/add/` | To add product in the cart |
| **DEL** | `api/cart/remove/id/` | To remove cart items|
| **POST** | `api/cart/checkout/` | To checkout |


#### Admin's Endpoints:
| HTTP | Endpoints | Action |
| --- | --- | --- |
| **GET** | `api/vendor/dashboard/` | To retrieve all the reports like how many products, orders etc. |
| **GET** | `api/vendor/admin-dashboard/` | To retrieve all the vendor staus, order status, revenue status and many more|
## Author

👤 **Symon**

- Github: [@sin1ter](https://github.com/sin1ter)
