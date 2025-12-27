import streamlit as st
import random

st.set_page_config(
    page_title="DECA Personal Financial Literacy Quizzes",
    page_icon="💰",
    layout="centered",
)

# ---------------------------------------------------------
# QUIZZES DATA
# ---------------------------------------------------------

QUIZZES = [
    {
        "name": "Quiz 1 – Budgeting & Saving Basics",
        "questions": [
            {
                "question": "1. What is the primary purpose of a personal budget?",
                "options": [
                    "To guarantee you never overspend",
                    "To plan and track income and expenses",
                    "To increase your credit score",
                    "To reduce your tax liability",
                ],
                "answer": 1,
                "explanation": "A budget is a spending plan that helps you allocate income toward expenses, savings, and goals.",
            },
            {
                "question": "2. Which of the following is an example of a fixed expense?",
                "options": [
                    "Electricity bill",
                    "Groceries",
                    "Rent or mortgage payment",
                    "Entertainment",
                ],
                "answer": 2,
                "explanation": "Fixed expenses stay relatively constant each month, such as rent or mortgage payments.",
            },
            {
                "question": "3. An emergency fund should primarily be used for:",
                "options": [
                    "Vacations and travel",
                    "Unplanned essential expenses like medical bills or car repairs",
                    "Holiday shopping",
                    "Investing in high-risk stocks",
                ],
                "answer": 1,
                "explanation": "Emergency funds are for unexpected, essential expenses to prevent going into debt.",
            },
            {
                "question": "4. A good rule of thumb for the size of an emergency fund is:",
                "options": [
                    "One week of expenses",
                    "One month of income",
                    "Three to six months of living expenses",
                    "Two years of income",
                ],
                "answer": 2,
                "explanation": "Many experts recommend three to six months of living expenses in an emergency fund.",
            },
            {
                "question": "5. Which statement about discretionary expenses is TRUE?",
                "options": [
                    "They are always required to maintain basic living standards",
                    "They are taxes taken out of your paycheck",
                    "They include wants like dining out or hobbies",
                    "They can never be changed",
                ],
                "answer": 2,
                "explanation": "Discretionary expenses are non-essential spending, such as entertainment and dining out.",
            },
            {
                "question": "6. Pay yourself first means:",
                "options": [
                    "Paying your bills before anything else",
                    "Saving or investing a portion of income before other spending",
                    "Paying off debt before saving",
                    "Spending on wants before needs",
                ],
                "answer": 1,
                "explanation": "Pay yourself first means automatically setting aside money for savings/investing before other expenses.",
            },
            {
                "question": "7. Which tool is MOST helpful for tracking daily spending?",
                "options": [
                    "A checking account only",
                    "A monthly bank statement you never review",
                    "A spending journal or budgeting app",
                    "Your memory",
                ],
                "answer": 2,
                "explanation": "A written or digital record of spending helps you see patterns and stay on budget.",
            },
            {
                "question": "8. What is the opportunity cost of buying a new phone today?",
                "options": [
                    "The price listed on the receipt",
                    "The sales tax on the purchase",
                    "Whatever you give up by not saving or spending that money on something else",
                    "The interest charged on your credit card",
                ],
                "answer": 2,
                "explanation": "Opportunity cost is the value of the next best alternative you give up when making a choice.",
            },
            {
                "question": "9. Net income is best defined as:",
                "options": [
                    "Income before any taxes or deductions",
                    "All sources of income plus bonuses",
                    "Income after taxes and deductions are subtracted",
                    "Only income from investments",
                ],
                "answer": 2,
                "explanation": "Net income, or take-home pay, is what remains after taxes and other deductions.",
            },
            {
                "question": "10. If your expenses are greater than your income, you are:",
                "options": [
                    "Operating at a surplus",
                    "Operating at a deficit",
                    "Living within your means",
                    "Improving your net worth",
                ],
                "answer": 1,
                "explanation": "When expenses exceed income, you have a budget deficit and may need to cut spending or increase income.",
            },
            {
                "question": "11. Which strategy is MOST effective to reduce impulse spending?",
                "options": [
                    "Shopping when you are hungry",
                    "Leaving credit cards at home and using a list",
                    "Browsing online stores late at night",
                    "Ignoring your budget",
                ],
                "answer": 1,
                "explanation": "Using a list and limiting access to payment methods helps reduce impulse buys.",
            },
            {
                "question": "12. A short-term financial goal is best described as one you want to achieve:",
                "options": [
                    "Within one year",
                    "In 5–10 years",
                    "Only after retirement",
                    "Over your lifetime",
                ],
                "answer": 0,
                "explanation": "Short-term goals typically have a time frame of up to one year.",
            },
            {
                "question": "13. Which type of account is MOST appropriate for an emergency fund?",
                "options": [
                    "Certificate of deposit (CD) with a 5-year term",
                    "Savings account with easy access",
                    "Retirement account with penalties for early withdrawal",
                    "Illiquid real estate investment",
                ],
                "answer": 1,
                "explanation": "Emergency funds should be accessible and relatively safe, so a liquid savings account is appropriate.",
            },
            {
                "question": "14. What is the FIRST step in creating a budget?",
                "options": [
                    "Cut all discretionary spending",
                    "Track and list your income and expenses",
                    "Apply for a new credit card",
                    "Set up automatic bill pay",
                ],
                "answer": 1,
                "explanation": "You must understand your income and expenses before you can create a realistic budget.",
            },
            {
                "question": "15. If you consistently underspend your budgeted amount for a category, you should:",
                "options": [
                    "Ignore the difference",
                    "Increase spending to match the budget",
                    "Adjust the budget and possibly move extra to savings",
                    "Cancel the category",
                ],
                "answer": 2,
                "explanation": "A budget should be flexible. If you underspend, you can adjust and direct extra money to goals like saving.",
            },
        ],
    },
    {
        "name": "Quiz 2 – Banking, Accounts & Payments",
        "questions": [
            {
                "question": "1. A checking account is primarily used for:",
                "options": [
                    "Long-term investing",
                    "Daily spending and paying bills",
                    "Holding retirement funds",
                    "Buying stocks and bonds",
                ],
                "answer": 1,
                "explanation": "Checking accounts are designed for frequent transactions, such as deposits, withdrawals, and bill payments.",
            },
            {
                "question": "2. Which is a common advantage of using direct deposit for your paycheck?",
                "options": [
                    "You receive your pay later",
                    "You avoid the need to cash a physical check",
                    "You earn double interest",
                    "You pay fewer taxes",
                ],
                "answer": 1,
                "explanation": "Direct deposit sends your paycheck electronically into your account, saving time and reducing risk of loss.",
            },
            {
                "question": "3. An overdraft occurs when:",
                "options": [
                    "You deposit more money than expected",
                    "Your account balance is negative due to spending more than you have",
                    "You forget to endorse a check",
                    "Your debit card is declined for fraud",
                ],
                "answer": 1,
                "explanation": "Overdrafts happen when withdrawals exceed your available balance, often resulting in fees.",
            },
            {
                "question": "4. Which payment method typically pulls money directly from your checking account?",
                "options": ["Debit card", "Credit card", "Store gift card", "Money order"],
                "answer": 0,
                "explanation": "Debit cards withdraw funds directly from your checking account at the time of purchase.",
            },
            {
                "question": "5. Why is it important to regularly reconcile your checking account?",
                "options": [
                    "To increase your credit limit",
                    "To ensure your records match the bank's and catch errors or fraud",
                    "To avoid paying taxes",
                    "To change your interest rate",
                ],
                "answer": 1,
                "explanation": "Reconciliation helps verify that your balance and transactions match the bank's records.",
            },
            {
                "question": "6. A Certificate of Deposit (CD) usually:",
                "options": [
                    "Allows unlimited withdrawals without penalty",
                    "Has a fixed term and may charge a penalty for early withdrawal",
                    "Is the same as a checking account",
                    "Has no interest rate",
                ],
                "answer": 1,
                "explanation": "CDs pay interest over a fixed term and can charge penalties if funds are withdrawn early.",
            },
            {
                "question": "7. The main difference between a credit card and a debit card is that:",
                "options": [
                    "Credit cards use borrowed money; debit cards use your own deposited funds",
                    "Debit cards always charge interest",
                    "Credit cards cannot be used online",
                    "Debit cards do not require a PIN",
                ],
                "answer": 0,
                "explanation": "Credit cards represent a loan; debit cards spend money directly from your bank account.",
            },
            {
                "question": "8. Which transaction is MOST likely to show as a 'pending' charge on your account?",
                "options": [
                    "A scheduled bill you haven't paid yet",
                    "A purchase made with your debit card that hasn't fully processed",
                    "Interest paid to your savings account",
                    "A paper check that was mailed but not received",
                ],
                "answer": 1,
                "explanation": "Pending charges show when a transaction is authorized but not fully settled yet.",
            },
            {
                "question": "9. Online banking allows you to:",
                "options": [
                    "Avoid keeping records of your spending",
                    "Instantly cancel federal taxes",
                    "View balances, transfer money, and pay bills electronically",
                    "Increase FDIC insurance limits automatically",
                ],
                "answer": 2,
                "explanation": "Online banking lets you manage accounts, pay bills, and transfer funds conveniently.",
            },
            {
                "question": "10. Which fee is MOST likely associated with an ATM transaction?",
                "options": [
                    "Annual percentage rate fee",
                    "Foreign transaction fee",
                    "Out-of-network ATM fee",
                    "Over-the-limit fee",
                ],
                "answer": 2,
                "explanation": "Using an ATM outside your bank's network can result in additional fees.",
            },
            {
                "question": "11. FDIC insurance on bank accounts is designed to:",
                "options": [
                    "Protect against market losses in stocks",
                    "Protect deposits if the bank fails, up to certain limits",
                    "Guarantee higher interest rates",
                    "Eliminate overdraft fees",
                ],
                "answer": 1,
                "explanation": "FDIC insurance protects depositors if a bank fails, up to the insured limit per depositor per bank.",
            },
            {
                "question": "12. A routing number on a check is used to:",
                "options": [
                    "Identify the account holder's address",
                    "Identify the specific financial institution",
                    "Provide the account balance",
                    "Show the amount of the check",
                ],
                "answer": 1,
                "explanation": "The routing number identifies the bank or credit union involved in the transaction.",
            },
            {
                "question": "13. A money market account typically:",
                "options": [
                    "Has no minimum balance requirements and no interest",
                    "Combines features of savings and checking, often with limited check writing",
                    "Is only available to businesses",
                    "Is used only for retirement savings",
                ],
                "answer": 1,
                "explanation": "Money market accounts often offer higher interest and limited check-writing privileges.",
            },
            {
                "question": "14. Which is the safest way to send money to pay a bill?",
                "options": [
                    "Mailing cash in an envelope",
                    "Using online bill pay through your bank",
                    "Giving your debit card to a friend",
                    "Posting your account details on social media",
                ],
                "answer": 1,
                "explanation": "Online bill pay is secure and traceable, reducing risk of loss or theft.",
            },
            {
                "question": "15. A benefit of using mobile payment apps (like digital wallets) is:",
                "options": [
                    "They guarantee you never overspend",
                    "They store and encrypt card information and can enable contactless payments",
                    "They eliminate the need for a bank account",
                    "They always reduce interest rates",
                ],
                "answer": 1,
                "explanation": "Mobile wallets can add convenience and security through tokenization and contactless payments.",
            },
        ],
    },
    {
        "name": "Quiz 3 – Credit, Debt & Loans",
        "questions": [
            {
                "question": "1. A credit score is best described as:",
                "options": [
                    "Your annual income",
                    "A numerical summary of your creditworthiness",
                    "The total amount of debt you owe",
                    "Your net worth",
                ],
                "answer": 1,
                "explanation": "A credit score reflects how likely you are to repay borrowed money based on your credit history.",
            },
            {
                "question": "2. Which factor has the BIGGEST impact on most credit scores?",
                "options": [
                    "Types of credit used",
                    "Payment history",
                    "Length of credit history",
                    "Number of recent credit inquiries",
                ],
                "answer": 1,
                "explanation": "On common scoring models, payment history is typically the most heavily weighted factor.",
            },
            {
                "question": "3. What does APR on a credit card represent?",
                "options": [
                    "Annual Principal Rate",
                    "Annual Percentage Rate, the yearly cost of borrowing",
                    "Average Payment Requirement",
                    "Amount Paid Recently",
                ],
                "answer": 1,
                "explanation": "APR is the yearly interest rate you pay on borrowed money, excluding most fees.",
            },
            {
                "question": "4. Minimum payment on a credit card is:",
                "options": [
                    "The maximum amount you must pay",
                    "The smallest amount you can pay to keep the account in good standing",
                    "The total balance due",
                    "The interest charge only",
                ],
                "answer": 1,
                "explanation": "Paying only the minimum keeps the account current but can lead to more interest over time.",
            },
            {
                "question": "5. Which is a sign of TOO much debt?",
                "options": [
                    "Paying your balance in full each month",
                    "Using less than 30% of your credit limit",
                    "Regularly missing payments or paying late fees",
                    "Checking your credit report yearly",
                ],
                "answer": 2,
                "explanation": "Late or missed payments indicate difficulty managing debt and hurt your credit profile.",
            },
            {
                "question": "6. Secured credit cards typically require:",
                "options": [
                    "No identification",
                    "A security deposit that serves as collateral",
                    "Very high income",
                    "A mortgage",
                ],
                "answer": 1,
                "explanation": "Secured cards use a deposit as collateral, helpful for building or rebuilding credit.",
            },
            {
                "question": "7. Which loan usually has the LOWEST interest rate, all else equal?",
                "options": [
                    "Payday loan",
                    "Credit card cash advance",
                    "Federal student loan",
                    "Rent-to-own agreement",
                ],
                "answer": 2,
                "explanation": "Federal student loans generally offer lower, fixed rates compared to many other forms of credit.",
            },
            {
                "question": "8. If you only make minimum payments on a large credit card balance, you will:",
                "options": [
                    "Pay off the balance quickly",
                    "Pay more interest and take longer to repay the debt",
                    "Avoid any interest charges",
                    "Improve your credit score immediately",
                ],
                "answer": 1,
                "explanation": "Minimum payments reduce the balance slowly, increasing total interest paid over time.",
            },
            {
                "question": "9. A cosigner on a loan:",
                "options": [
                    "Is not responsible for repayment",
                    "Agrees to repay the loan if the borrower fails to do so",
                    "Only receives rewards points",
                    "Cannot be affected by missed payments",
                ],
                "answer": 1,
                "explanation": "Cosigners legally share responsibility; late or missed payments affect their credit too.",
            },
            {
                "question": "10. What is credit utilization?",
                "options": [
                    "The total number of accounts you have",
                    "The percentage of your available credit you are using",
                    "Your total outstanding debt",
                    "The length of time you've had credit",
                ],
                "answer": 1,
                "explanation": "Credit utilization is your balance divided by your total credit limit, expressed as a percentage.",
            },
            {
                "question": "11. A payday loan is generally considered risky because:",
                "options": [
                    "It has no due date",
                    "It usually has very high fees and interest rates",
                    "It must be used for education",
                    "It improves your credit score automatically",
                ],
                "answer": 1,
                "explanation": "Payday loans charge extremely high costs, which can trap borrowers in cycles of debt.",
            },
            {
                "question": "12. Which action is MOST likely to improve your credit score over time?",
                "options": [
                    "Closing your oldest credit account",
                    "Consistently paying all bills on time",
                    "Maxing out credit cards regularly",
                    "Applying for several new cards at once",
                ],
                "answer": 1,
                "explanation": "On-time payments are the single most important habit for building a strong credit history.",
            },
            {
                "question": "13. Defaulting on a loan means:",
                "options": [
                    "Paying more than required",
                    "Refinancing the loan",
                    "Failing to make payments as agreed over a period of time",
                    "Paying off the balance early",
                ],
                "answer": 2,
                "explanation": "Default occurs when a borrower fails to meet the legal obligations of the loan agreement.",
            },
            {
                "question": "14. An amortization schedule shows:",
                "options": [
                    "Only the total interest cost",
                    "How each payment is split between principal and interest over time",
                    "Your credit score by month",
                    "The bank's profit",
                ],
                "answer": 1,
                "explanation": "Amortization tables break down each payment into principal and interest components.",
            },
            {
                "question": "15. To avoid paying interest on a credit card purchase, you generally must:",
                "options": [
                    "Make only the minimum payment",
                    "Pay the full statement balance by the due date",
                    "Transfer the balance to another card",
                    "Ignore the bill until next month",
                ],
                "answer": 1,
                "explanation": "Paying the full statement balance each cycle usually avoids interest on new purchases.",
            },
        ],
    },
    {
        "name": "Quiz 4 – Investing & Wealth Building",
        "questions": [
            {
                "question": "1. The main reason people invest money instead of just saving is to:",
                "options": [
                    "Increase risk with no benefit",
                    "Potentially earn higher returns over the long term",
                    "Guarantee that they will never lose money",
                    "Avoid paying any taxes",
                ],
                "answer": 1,
                "explanation": "Investing can help money grow faster than traditional savings, though it involves risk.",
            },
            {
                "question": "2. Diversification in investing means:",
                "options": [
                    "Putting all your money in one stock",
                    "Spreading investments across different assets to reduce risk",
                    "Holding only cash",
                    "Borrowing to invest",
                ],
                "answer": 1,
                "explanation": "Diversification reduces risk by not relying on a single investment.",
            },
            {
                "question": "3. A stock represents:",
                "options": [
                    "Debt you owe to a company",
                    "Ownership in a company",
                    "A guaranteed fixed interest payment",
                    "A government tax",
                ],
                "answer": 1,
                "explanation": "Stock shares represent partial ownership in a corporation.",
            },
            {
                "question": "4. A bond is best described as:",
                "options": [
                    "Ownership in a company",
                    "A type of savings account",
                    "A loan made by the investor to a government or corporation",
                    "A checking account",
                ],
                "answer": 2,
                "explanation": "When you buy a bond, you are lending money to the issuer in exchange for interest.",
            },
            {
                "question": "5. The risk–return tradeoff means:",
                "options": [
                    "Lower risk always leads to higher returns",
                    "Higher potential returns usually come with higher risk",
                    "Risk and return are not related",
                    "You can get high returns with no risk",
                ],
                "answer": 1,
                "explanation": "Investments with greater potential return typically involve greater risk of loss.",
            },
            {
                "question": "6. Compound interest means:",
                "options": [
                    "Interest is earned only on the original principal",
                    "Interest is earned on principal plus previously earned interest",
                    "Interest rates never change",
                    "Interest applies only to loans, not savings",
                ],
                "answer": 1,
                "explanation": "Compound interest accelerates growth because you earn interest on interest.",
            },
            {
                "question": "7. A mutual fund is:",
                "options": [
                    "A type of insurance policy",
                    "A pooled investment that owns a diversified portfolio of assets",
                    "A government fee",
                    "A type of credit card",
                ],
                "answer": 1,
                "explanation": "Mutual funds combine money from many investors to buy a diversified set of holdings.",
            },
            {
                "question": "8. An index fund typically aims to:",
                "options": [
                    "Beat the market through active trading",
                    "Match the performance of a specific market index",
                    "Avoid all market risk",
                    "Invest only in cash",
                ],
                "answer": 1,
                "explanation": "Index funds passively track a market index like the S&P 500.",
            },
            {
                "question": "9. Time in the market is generally considered more important than:",
                "options": [
                    "Diversification",
                    "Dollar-cost averaging",
                    "Timing the market",
                    "Saving consistently",
                ],
                "answer": 2,
                "explanation": "Trying to perfectly time market highs and lows is difficult; long-term investing tends to be more effective.",
            },
            {
                "question": "10. A retirement account like a 401(k) or IRA often provides benefits such as:",
                "options": [
                    "Tax advantages and long-term growth potential",
                    "Guaranteed daily profits",
                    "No contribution limits",
                    "Immediate penalty-free withdrawals",
                ],
                "answer": 0,
                "explanation": "Retirement accounts may offer tax-deferred or tax-free growth, but have contribution limits and withdrawal rules.",
            },
            {
                "question": "11. Liquidity refers to:",
                "options": [
                    "How safe an investment is from fraud",
                    "How quickly you can convert an investment to cash without significant loss in value",
                    "The interest rate on a loan",
                    "The amount of dividends paid",
                ],
                "answer": 1,
                "explanation": "Highly liquid assets, like cash, are easy to convert and use quickly.",
            },
            {
                "question": "12. Dollar-cost averaging is a strategy where you:",
                "options": [
                    "Invest a fixed amount at regular intervals regardless of market conditions",
                    "Invest only when prices are low",
                    "Invest only once at the beginning",
                    "Borrow money to invest more",
                ],
                "answer": 0,
                "explanation": "Dollar-cost averaging smooths out the impact of market volatility over time.",
            },
            {
                "question": "13. Inflation risk means:",
                "options": [
                    "Your investment can never lose value",
                    "Your purchasing power may decrease if returns don’t keep up with rising prices",
                    "Prices will always fall",
                    "Interest rates will stay the same",
                ],
                "answer": 1,
                "explanation": "Inflation erodes the value of money, so investments must outpace inflation to grow real wealth.",
            },
            {
                "question": "14. A speculative investment is one that:",
                "options": [
                    "Has low risk and guaranteed returns",
                    "Has high potential return but very high risk and uncertainty",
                    "Is insured by the government",
                    "Is only available to retirees",
                ],
                "answer": 1,
                "explanation": "Speculative investments may offer big gains but also carry a high chance of loss.",
            },
            {
                "question": "15. Before investing, it is MOST important to:",
                "options": [
                    "Borrow money to start sooner",
                    "Understand your financial goals, time horizon, and risk tolerance",
                    "Only listen to friends' stock tips",
                    "Ignore diversification",
                ],
                "answer": 1,
                "explanation": "Your goals and risk tolerance should guide your investment choices.",
            },
        ],
    },
    {
        "name": "Quiz 5 – Insurance, Taxes & Financial Planning",
        "questions": [
            {
                "question": "1. The main purpose of insurance is to:",
                "options": [
                    "Guarantee profits",
                    "Protect against financial loss from unexpected events",
                    "Increase your credit score",
                    "Avoid paying taxes",
                ],
                "answer": 1,
                "explanation": "Insurance transfers financial risk from you to the insurance company in exchange for premiums.",
            },
            {
                "question": "2. A deductible in an insurance policy is:",
                "options": [
                    "The monthly premium you pay",
                    "The amount you must pay out-of-pocket before insurance covers the rest",
                    "The total value of the policy",
                    "The tax refund you receive",
                ],
                "answer": 1,
                "explanation": "You pay the deductible first; the insurer then covers costs according to the policy.",
            },
            {
                "question": "3. Health insurance primarily helps you manage:",
                "options": [
                    "Auto repair costs",
                    "Medical expenses and healthcare costs",
                    "Home maintenance costs",
                    "Investment fees",
                ],
                "answer": 1,
                "explanation": "Health insurance reduces the financial impact of medical services and treatments.",
            },
            {
                "question": "4. Auto liability insurance typically covers:",
                "options": [
                    "Damage to your own car only",
                    "Damage and injuries you cause to others in an accident",
                    "Routine oil changes",
                    "Car washes",
                ],
                "answer": 1,
                "explanation": "Liability coverage pays for others' injuries or property damage if you are at fault.",
            },
            {
                "question": "5. Life insurance is MOST important for individuals who:",
                "options": [
                    "Have no dependents and no debts",
                    "Have dependents who rely on their income",
                    "Are retired and have no expenses",
                    "Do not plan for the future",
                ],
                "answer": 1,
                "explanation": "Life insurance helps protect dependents financially if the policyholder dies.",
            },
            {
                "question": "6. A premium in insurance is:",
                "options": [
                    "The amount of coverage you receive",
                    "The regular payment you make to maintain your policy",
                    "The refund sent by the insurer",
                    "The deductible you pay",
                ],
                "answer": 1,
                "explanation": "Premiums are the periodic payments required to keep insurance coverage in force.",
            },
            {
                "question": "7. The purpose of a W-4 form when starting a job is to:",
                "options": [
                    "Apply for health insurance",
                    "Tell your employer how much federal income tax to withhold from your paycheck",
                    "Request a pay raise",
                    "Choose your retirement plan",
                ],
                "answer": 1,
                "explanation": "Your W-4 determines your tax withholding based on your situation.",
            },
            {
                "question": "8. Gross pay is:",
                "options": [
                    "Pay after taxes and deductions",
                    "Pay before any taxes or deductions are taken out",
                    "Only overtime pay",
                    "Only bonus pay",
                ],
                "answer": 1,
                "explanation": "Gross pay is total earnings before taxes, benefits, and other deductions.",
            },
            {
                "question": "9. Which of the following is typically a required payroll tax?",
                "options": ["Sales tax", "Property tax", "Social Security tax", "Estate tax"],
                "answer": 2,
                "explanation": "Payroll taxes commonly include Social Security and Medicare, withheld from paychecks.",
            },
            {
                "question": "10. A tax refund means:",
                "options": [
                    "You underpaid your taxes",
                    "You paid more tax during the year than you owed",
                    "You paid exactly the right amount of tax",
                    "You are exempt from future taxes",
                ],
                "answer": 1,
                "explanation": "Refunds occur when total tax payments exceed your final tax liability.",
            },
            {
                "question": "11. A will is a legal document that:",
                "options": [
                    "Defines how your assets should be distributed after death",
                    "Sets your insurance premiums",
                    "Calculates your credit score",
                    "Determines your tax bracket",
                ],
                "answer": 0,
                "explanation": "A will provides instructions for distributing your property and caring for dependents.",
            },
            {
                "question": "12. Estate planning is primarily concerned with:",
                "options": [
                    "Maximizing your credit card rewards",
                    "Managing and distributing your assets during life and after death",
                    "Choosing a bank",
                    "Avoiding all insurance",
                ],
                "answer": 1,
                "explanation": "Estate planning ensures your wishes are followed for assets, healthcare, and dependents.",
            },
            {
                "question": "13. A long-term financial plan should include:",
                "options": [
                    "Only short-term goals like buying clothes",
                    "Savings, investing, insurance, and retirement planning",
                    "Daily spending decisions only",
                    "Random purchases",
                ],
                "answer": 1,
                "explanation": "Comprehensive planning covers goals, protection, and future income needs.",
            },
            {
                "question": "14. A benefit of employer-sponsored retirement plans (like a 401(k)) is that:",
                "options": [
                    "They are not regulated",
                    "Some employers offer matching contributions to your savings",
                    "You can withdraw anytime without penalties",
                    "They are insured against market losses",
                ],
                "answer": 1,
                "explanation": "Employer matches can significantly boost your retirement savings.",
            },
            {
                "question": "15. The primary advantage of starting to save for retirement in your early 20s is:",
                "options": [
                    "You will never experience market downturns",
                    "You benefit more from compound interest over a longer period",
                    "You pay no taxes ever",
                    "You can stop working immediately",
                ],
                "answer": 1,
                "explanation": "The earlier you start, the more time compound growth has to work in your favor.",
            },
        ],
    },
]

# ---------------------------------------------------------
# QUIZ RENDERING FUNCTION
# ---------------------------------------------------------


def render_quiz(quiz_index: int):
    quiz = QUIZZES[quiz_index]
    st.header(quiz["name"])

    # Toggle for per-question feedback
    feedback_mode = st.checkbox("Show feedback after each question", value=False)

    # Initialize session state
    if "responses" not in st.session_state:
        st.session_state["responses"] = {}
    if quiz_index not in st.session_state["responses"]:
        st.session_state["responses"][quiz_index] = {}

    # Randomize question order once per quiz load
    if "order" not in st.session_state["responses"][quiz_index]:
        order = list(range(len(quiz["questions"])))
        random.shuffle(order)
        st.session_state["responses"][quiz_index]["order"] = order

    order = st.session_state["responses"][quiz_index]["order"]
    responses = st.session_state["responses"][quiz_index]

    st.write(
        "Select your answers for all questions, then click **Submit Quiz** at the bottom."
    )

    # Progress bar
    answered = sum(1 for i in order if responses.get(f"q_{i}") is not None)
    progress = answered / len(order) if len(order) > 0 else 0
    st.progress(progress)

    # Render questions
    for i in order:
        q = quiz["questions"][i]
        st.markdown(f"**{q['question']}**")

        key = f"q_{i}"
        current_value = responses.get(key, None)

        # No default selection
        choice = st.radio(
            label="",
            options=list(range(len(q["options"]))),
            format_func=lambda idx, opts=q["options"]: opts[idx],
            index=current_value if current_value is not None else None,
            key=key,
        )

        responses[key] = choice

        # Per-question feedback
        if feedback_mode and choice is not None:
            if choice == q["answer"]:
                st.success("Correct!")
            else:
                st.error("Incorrect.")
            st.info(f"Explanation: {q['explanation']}")

        st.markdown("---")

    # Submit button
    if st.button("Submit Quiz"):
        score = 0
        total = len(order)
        st.subheader("Results")

        for i in order:
            q = quiz["questions"][i]
            selected = responses.get(f"q_{i}", None)
            correct = q["answer"]

            if selected == correct:
                score += 1
                st.markdown(f"✅ **Correct:** {q['question']}")
            else:
                st.markdown(f"❌ **Incorrect:** {q['question']}")

            st.markdown(
                f"- **Your answer:** {q['options'][selected] if selected is not None else 'No answer'}"
            )
            st.markdown(f"- **Correct answer:** {q['options'][correct]}")
            st.markdown(f"- **Explanation:** {q['explanation']}")
            st.markdown("---")

        st.success(f"Your score: **{score} / {total}** ({round(score/total*100)}%)")


# ---------------------------------------------------------
# MAIN APP LAYOUT
# ---------------------------------------------------------

st.title("DECA Personal Financial Literacy Quizzes")
st.caption(
    "Practice personal financial literacy concepts with five DECA-style multiple-choice quizzes."
)

quiz_names = [q["name"] for q in QUIZZES]
selected_quiz_name = st.selectbox("Choose a quiz:", quiz_names)
selected_index = quiz_names.index(selected_quiz_name)

render_quiz(selected_index)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
<br><br>
<div style='text-align: center; color: gray; font-size: 14px;'>
    App developed by <strong>Sathvik Kakarla</strong>
</div>
""",
    unsafe_allow_html=True,
)
