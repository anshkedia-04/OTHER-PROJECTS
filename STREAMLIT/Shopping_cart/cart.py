import streamlit as st

# Data for dropdown
items = [
    {"name": "Smartphone", "price": 699, "category": "Electronics"},
    {"name": "Laptop", "price": 1299, "category": "Electronics"},
    {"name": "Smartwatch", "price": 199, "category": "Electronics"},
    {"name": "Blender", "price": 150, "category": "Kitchenware"},
    {"name": "Sofa", "price": 500, "category": "Furniture"},
    {"name": "Dining Table", "price": 750, "category": "Furniture"},
    {"name": "T-Shirt", "price": 25, "category": "Clothing"},
    {"name": "Jacket", "price": 100, "category": "Clothing"},
    { "name": "Sneakers", "price": 80, "category": "fashion" },
    { "name": "Handbag", "price": 60, "category": "fashion" },
    { "name": "Sofa", "price": 500, "category": "home items" },
    { "name": "Dining Table", "price": 750, "category": "home items" },
    { "name": "Desk Lamp", "price": 40, "category": "home items" },
    { "name": "Curtains", "price": 70, "category": "home items" },
    { "name": "Rug", "price": 120, "category": "home items" },
    { "name": "Tablet", "price": 350, "category": "electronics" },
    { "name": "Blender", "price": 150, "category": "home items" },
    { "name": "Sunglasses", "price": 120, "category": "fashion" },
    { "name": "Gaming Console", "price": 499, "category": "electronics" },
    { "name": "Bookshelf", "price": 200, "category": "home items" }
]

# Streamlit layout
st.set_page_config(layout="wide")

# Header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        color: black;
        background-color: #4CAF50;
        padding: 10px;
        text-align: center;
    }
    </style>
    <div class="header">Hello-Mart</div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Dropdown
st.sidebar.header("Dropdown List for Items")
categories = ["All"] + sorted(set(item["category"] for item in items))
selected_category = st.sidebar.selectbox("Select a Category", categories)

if selected_category == "All":
    filtered_items = items
else:
    filtered_items = [item for item in items if item["category"] == selected_category]

selected_items = st.sidebar.multiselect(
    "Select Products:", [item["name"] for item in filtered_items]
)

# Main Content
st.markdown("<h3 style='text-align: center;'>Selected Products</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

selected_products = [item for item in items if item["name"] in selected_items]

for index, product in enumerate(selected_products):
    with [col1, col2, col3][index % 3]:
        st.markdown(
            f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; text-align: center; background-color: black;">
                <h4>{product["name"]}</h4>
                <p><b>Price:</b> ${product["price"]}</p>
                <p><b>Category:</b> {product["category"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #333;
        color: white;
        font-size: 20px;
        text-align: center;
        padding: 10px;
        margin-left:150px;
    }
    </style>
    <div class="footer">Have a great day</div>
    """,
    unsafe_allow_html=True,
)
