from .models import Product, ShippingBox


def recommend_box(items):
    total_weight = 0
    total_volume = 0
    max_length = 0
    max_width = 0
    total_height = 0

    for item in items:
        try:
            product = Product.objects.get(name__iexact=item["product_name"])
        except Product.DoesNotExist:
            return {
                "error": f"Product '{item['product_name']}' not found."
            }
        qty = item["quantity"]

        total_weight += product.weight * qty
        total_volume += (
            product.length *
            product.width *
            product.height *
            qty
        )

        max_length = max(max_length, product.length)
        max_width = max(max_width, product.width)
        total_height += product.height * qty

    suitable_boxes = []

    # THIS IS THE FIX
    for box in ShippingBox.objects.all():
        if (
            box.inner_length >= max_length and
            box.inner_width >= max_width and
            box.inner_height >= total_height and
            box.max_weight >= total_weight
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda x: (x.cost, x.volume()))

    return suitable_boxes[0]