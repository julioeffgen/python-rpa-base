# It's a really simple Python RPA with selenium webdriver

The objective of this RPA is to extract the value of USD and EUR from the day before the execution day.

To do this, the RPA has to access these websites:
- USD: https://br.investing.com/currencies/usd-brl-historical-data
- EUR: https://br.investing.com/currencies/eur-brl-historical-data

# Rules
- Error safe: The RPA has to predict and treat exceptions that can happen during the process
- Cookies banner: Make sure that permission banner for cookies was correctly closed
- Registration banner: Make sure that registration banner was dismissed, if necessary
- Collect the information by the follow steps:
    - Extract the USD info by first
        - After extract USD info, the next iteration have to extract EUR info
    - The RPA needs to search the result by the date range
        - `Target date` is one day before the execution date
        - `Start date` is the execution date
        - `End date` is the target date
    - With the results filtered, the RPA has to select only the line of the `target date`
    - If the result table has no line equal the `target date`, the RPA needs to end the execution with success
- All data and orchestration queues has to be done using MongoDB
