from savingsAccount import SavingsAccount

st.set_page_config(page_title = "Bank App", layout = 'centered')

savings : SavingsAccount = SavingsAccount (200000)

with st.form ('savings_form'):
    amount = st.number_input ('Enter Amount')
    operations = st.selectbox ('Deposite or Withdraw', ("Deposite", "Withdraw"))
    submit = st.form_submit.button('Submit')

    if submit and operations == 'Withdraw':
        with st.spinner('Processing...'):
        savings.(amount)


        print(savings.balance)
