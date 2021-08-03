#Checkout Process
1. Cart -> Checkout View
    - Login/Registor or Email (as Guest)
    - Shipping address
    - Billing info
        - Billing address
        - Credit Card / Payment
2. Billing App/Component
    - Billing Profile
        - User or Email (Guest Email)
        - generate payment processor token (Stripe or Braintree)
3. Orders / Invoices Component
    - Connecting the billing profile
    - Shipping / Billing Address
    - Cart
    - Status -- Shipped? Cancelled?