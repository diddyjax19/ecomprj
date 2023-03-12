from django import views
from django.urls import path, include
from core.views import add_to_cart, add_to_wishlist, ajax_add_review, ajax_contact_form, cart_view, category_list_view, category_product_list__view, checkout_view, customer_dashboard, delete_item_from_cart, filter_product, index, make_address_default, order_detail, payment_completed_view, payment_failed_view, product_detail_view, product_list_view, remove_wishlist, search_view, tag_list, update_cart, vendor_detail_view, vendor_list_view, wishlist_view, contact, about_us, purchase_guide, privacy_policy, terms_of_service

app_name = "core"

urlpatterns = [

    # Homepage path
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product-detail"),

    # Category path
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),

    # Vendor path
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>/", vendor_detail_view, name="vendor-detail"),

    # Tags path
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    # Review 
    path("ajax-add-review/<int:pid>/", ajax_add_review, name="ajax-add-review"),

    # Search path
    path("search/", search_view, name="search"),

    # Filter product  path
    path("filter-products/", filter_product, name="filter-product"),

    # Add to cart path
    path("add-to-cart/", add_to_cart, name="add-to-cart"),

    # Cart Page path
    path("cart/", cart_view, name="cart"),

    # Delete Item path
    path("delete-from-cart/", delete_item_from_cart, name="delete-from-cart"),

    # Update cart pah\th
    path("update-cart/", update_cart, name="update-cart"),

      # Checkout  URL path
    path("checkout/", checkout_view, name="checkout"),

    # Paypal path
    path('paypal/', include('paypal.standard.ipn.urls')),

    # Successful payment
    path("payment-completed/", payment_completed_view, name="payment-completed"),

    # Payment Failed path
    path("payment-failed/", payment_failed_view, name="payment-failed"),

    # Dahboard path
    path("dashboard/", customer_dashboard, name="dashboard"),

    # Order Detail path
    path("dashboard/order/<int:id>", order_detail, name="order-detail"),

    # Making default address
    path("make-default-address/", make_address_default, name="make-default-address"),

    # wishlist path
    path("wishlist/", wishlist_view, name="wishlist"),

    # adding to wishlist path
    path("add-to-wishlist/", add_to_wishlist, name="add-to-wishlist"),


    # Remvoing from wishlist path
    path("remove-from-wishlist/", remove_wishlist, name="remove-from-wishlist"),

  # contact page
    path("contact/", contact, name="contact"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),

  # about us
    path("about_us/", about_us, name="about_us"),

    # purchase guide
    path("purchase_guide/", purchase_guide, name="purchase_guide"),

    # privacy policy
    path("privacy_policy/", privacy_policy, name="privacy_policy"),

    # Terms of service
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
]