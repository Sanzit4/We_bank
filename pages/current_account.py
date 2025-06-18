import streamlit as st


from CurrentAccount import CurrentAccount
from pages.savings_account import operations, sumbit
from savingsaccount import balance

if 'account' not in st.session_state:
    st.session_state.account = CurrentAccount(balance= 500000)
st.set_page_config(page_title=" Current Account", layout = "centered")
st.title("Current Account")

balance_placeholder = st.empty()
balance_placeholder.subheader(f"BALANCE: ₦{st.session_state.account.balance}")
with st.form("current_account_form"):
    amount = st.number_input("Enter amount",min_value=0, step=100)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    sumbit = st.form_submit_button("Sumbit")

    if sumbit:
        try:
            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.success(f"Successfuly Depositted ₦{amount}")
            elif operations == "Withdraw":
                st.session_state.account.withdraw(amount)
                st.success(f"Successfully Withdrew ₦{amount}!")
            balance_placeholder.subheader(f"Balance: ₦{st.session_state.account.balance}")
        except ValueError as e:
            st.error(str(e))
