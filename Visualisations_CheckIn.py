import plotly.express as px
import pandas as pd

# Load the data
file_path = 'Avail Grower Details.xlsx'
checkin_data = pd.read_excel(file_path, sheet_name='Form responses 2')

# First-Year Check-In Data
# Histograms for First-Year Check-In Data
fig_checkin_family_size = px.histogram(
    checkin_data, x='Family Size',
    title='1st Year Check-In: Family Size Distribution',
    color_discrete_sequence=['yellowgreen'],
    labels={'value': 'Family Size'}
)
fig_checkin_family_size.update_layout(bargap=0.1)
fig_checkin_family_size.update_yaxes(title_text='Count of Growers') 

fig_checkin_land_rights = px.histogram(
    checkin_data, x='Number of family members with rights to use land',
    title='1st Year Check-In: Family Members with Land Rights',
    color_discrete_sequence=['seagreen'],
    labels={'value': 'Family Members with Land Rights'}
)
fig_checkin_land_rights.update_layout(bargap=0.1)
fig_checkin_land_rights.update_yaxes(title_text='Count of Growers') 

fig_checkin_children_school = px.histogram(
    checkin_data, x='Number of Children at School',
    title='1st Year Check-In: Number of Children at School',
    color_discrete_sequence=['green'],
    labels={'value': 'Children at School'}
)
fig_checkin_children_school.update_layout(bargap=0.1)
fig_checkin_children_school.update_yaxes(title_text='Count of Growers') 

fig_checkin_meals_per_day = px.histogram(
    checkin_data, x='Average number of meals per day in households',
    title='1st Year Check-In: Average Meals per Day',
    color_discrete_sequence=['yellowgreen'],
    labels={'value': 'Meals Per Day'}
)
fig_checkin_meals_per_day.update_layout(bargap=0.1)
fig_checkin_meals_per_day.update_yaxes(title_text='Count of Growers') 

# Pie Charts for 1st Year Check-In
fig_checkin_production_status = px.pie(
    checkin_data, names='Status of Production Systems',
    title='1st Year Check-In: Status of Production Systems',
    color_discrete_sequence=px.colors.sequential.Greens
)

fig_checkin_pest_management = px.pie(
    checkin_data, names='Do you use environmentally friendly pest and disease-management methods?',
    title='1st Year Check-In: Environmentally Friendly Pest Management',
    color_discrete_sequence=['green', 'yellowgreen']
)

# Boxplots for 1st Year Check-In
fig_checkin_annual_income = px.box(
    checkin_data, y='Annual Income',
    title='1st Year Check-In: Annual Income Distribution',
    color_discrete_sequence=['mediumseagreen'],
    labels={'value': 'Annual Income (UGX)'}
)

fig_checkin_cultivated_land = px.box(
    checkin_data, y='Area of Cultivated Land',
    title='1st Year Check-In: Area of Cultivated Land Distribution',
    color_discrete_sequence=['green'],
    labels={'value': 'Area of Cultivated Land (acres)'},
    range_y = [1,20]
)

fig_checkin_production_size = px.box(
    checkin_data, y=' Size of Production Cultivated',
    title='1st Year Check-In: Size of Production Cultivated',
    color_discrete_sequence=['yellowgreen'],
    labels={'value': 'Size of Production Cultivated (kg)'}
)