# Test Cases

## Model Tests

- Product creation
- ShippingBox creation

## Serializer Tests

- Valid OrderItemSerializer
- Invalid serializer input

## Service Tests

- Recommend suitable shipping box
- No suitable box available

## API Tests

GET /api/products/

Expected:
200 OK

---

GET /api/boxes/

Expected:
200 OK

---

POST /api/recommend-box/

Expected:
Returns best shipping box.

---

Invalid Product Name

Expected:
Returns validation error or not found response.

---

Invalid Quantity

Expected:
Returns serializer validation error.
