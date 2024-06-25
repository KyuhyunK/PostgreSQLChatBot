import streamlit as st

MYSQL_HOST = st.secrets["mysql"]["MYSQL_HOST"]
MYSQL_USER = st.secrets["mysql"]["MYSQL_USER"]
MYSQL_PASSWORD = st.secrets["mysql"]["MYSQL_PASSWORD"]
MYSQL_DATABASE = st.secrets["mysql"]["MYSQL_DATABASE"]
OPENAI_API_KEY = st.secrets["openai"]["OPENAI_API_KEY"]


column_descriptions = {
    "id": "Unique identifier for each record",
    "sku": "Stock Keeping Unit, unique identifier for each product",
    "asin": "Amazon Standard Identification Number, unique identifier for Amazon products",
    "listing_state": "State of the listing (e.g., active, inactive)",
    "cost": "Cost of the item",
    "quantity": "Number of units available",
    "min_price": "Minimum price of the item",
    "max_price": "Maximum price of the item",
    "listed_price": "Price at which the item is listed",
    "avg_selling_price": "Average selling price of the item",
    "total_revenue": "Total revenue generated by the item",
    "total_revenue_prev": "Previous period total revenue",
    "total_revenue_diff": "Difference in revenue between periods",
    "total_profit": "Total profit generated by the item",
    "total_profit_prev": "Previous period total profit",
    "total_profit_diff": "Difference in profit between periods",
    "total_ordered_items": "Total number of items ordered",
    "profit_margin": "Profit margin for the item",
    "roi": "Return on investment",
    "fba_inbound_quantity": "Quantity of items inbound to FBA (Fulfillment by Amazon)",
    "pkg_weight": "Package weight",
    "pkg_length": "Package length",
    "pkg_width": "Package width",
    "pkg_height": "Package height",
    "pkg_volume": "Package volume",
    "return_rate": "Rate of item returns",
    "profit_after_returns": "Profit after accounting for returns",
    "revenue_after_returns": "Revenue after accounting for returns",
    "return_items": "Number of items returned",
    "cost_of_returns": "Cost associated with returns",
    "profit_margin_at_min": "Profit margin at minimum price",
    "profit_margin_at_max": "Profit margin at maximum price",
    "fulfillment_fee": "Fee for fulfillment services",
    "amazon_fees": "Fees charged by Amazon",
    "net_proceeds": "Net proceeds after fees",
    "total_COGS": "Total cost of goods sold",
    "total_fulfillment_fees": "Total fulfillment fees",
    "total_return_processing_fees": "Total return processing fees",
    "returned_items_cost": "Cost of returned items",
    "cost_of_return": "Cost incurred for returning items",
    "total_referral_fees": "Total referral fees",
    "year": "Year that data was pulled from",
    "quarter": "Quarter that data was pulled from"
}