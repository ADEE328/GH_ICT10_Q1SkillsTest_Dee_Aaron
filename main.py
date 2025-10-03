from pyscript import display, document

def create_order(event=None):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    items = document.querySelectorAll("input[type='checkbox']:checked")
    total = sum([int(item.getAttribute("data-price")) for item in items])

    # Validation
    if not name or not address or not contact:
        document.getElementById("output").innerHTML = "Please fill in all customer details."
        return
    
    if len(items) == 0:
        document.getElementById("output").innerHTML = "Please select at least one food item."
        return

    # Final summary (replace old output instead of appending)
    order_summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Total: ₱ {total:.2f}
    """
    document.getElementById("output").innerHTML = order_summary
