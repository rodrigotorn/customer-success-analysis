# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Test

# %%
import pandas as pd
import duckdb

# %%
customer_revenue_monthly = pd.read_csv(
  'input_data/customer_revenue_monthly.csv',
  sep=',',
  decimal='.'
)

dim_customer = pd.read_csv(
  'input_data/dim_customer.csv',
  sep=',',
  decimal='.'
)

# %%
duckdb.query("""
SELECT * FROM customer_revenue_monthly crm
inner join dim_customer dc on dc.customer_id = crm.customer_id
limit 1
""").df()

# %%
duckdb.query("""
SELECT * FROM customer_revenue_monthly limit 1
""").df()

# %%
duckdb.query("""
SELECT * FROM dim_customer limit 1
""").df()

# %%
