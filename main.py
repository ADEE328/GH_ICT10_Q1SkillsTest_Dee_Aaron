from pyscript import display, document

def create_order(event=None):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    items = document.querySelectorAll("input[type='checkbox']:checked")
    total = sum([int(item.getAttribute("data-price")) for item in items])

    if not name or not address or not contact:
        document.getElementById("output").innerHTML = "Please fill in all customer details."
        return
    
    if len(items) == 0:
        document.getElementById("output").innerHTML = "Please select at least one food item."
        return
        
    order_summary = f"""
    Order for: {name}<br>
    Address: {address}<br>
    Contact number: {contact}<br>
    Total: ₱ {total:.2f}
    """
    document.getElementById("output").innerHTML = order_summary

