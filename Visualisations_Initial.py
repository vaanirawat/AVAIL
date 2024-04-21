import plotly.express as px
import pandas as pd

# Load the data
file_path = 'Avail Grower Details.xlsx'
initial_data = pd.read_excel(file_path, sheet_name='Form responses 1')

# Inital Data
# Histograms for Initial Data
fig_initial_family_size = px.histogram(
    initial_data, x='Family Size',
    title='Initial Data: Family Size Distribution',
    color_discrete_sequence=['seagreen'],
    labels={'value': 'Family Size'},
    barnorm=''
)
fig_initial_family_size.update_layout(bargap=0.1) 
fig_initial_family_size.update_yaxes(title_text='Count of Growers') 

fig_initial_land_rights = px.histogram(
    initial_data, x='Number of family members with rights to use land',
    title='Initial Data: Family Members with Land Rights',
    color_discrete_sequence=['mediumseagreen'],
    labels={'value': 'Family Members with Land Rights'}
)
fig_initial_land_rights.update_layout(bargap=0.1)
fig_initial_land_rights.update_yaxes(title_text='Count of Growers')

fig_initial_children_school = px.histogram(
    initial_data, x='Number of Children at School',
    title='Initial Data: Number of Children at School',
    color_discrete_sequence=['yellowgreen'],
    labels={'value': 'Children at School'}
)
fig_initial_children_school.update_layout(bargap=0.1)
fig_initial_children_school.update_yaxes(title_text='Count of Growers')

fig_initial_meals_per_day = px.histogram(
    initial_data, x='Average number of meals per day in households',
    title='Initial Data: Average Meals per Day',
    color_discrete_sequence=['green'],
    labels={'value': 'Meals Per Day'}
)
fig_initial_meals_per_day.update_layout(bargap=0.1)
fig_initial_meals_per_day.update_yaxes(title_text='Count of Growers')

# Pie Charts for Initial Data
fig_initial_production_status = px.pie(
    initial_data, names='Status of Production Systems',
    title='Initial Data: Status of Production Systems',
    color_discrete_sequence=px.colors.sequential.Greens
)

fig_initial_pest_management = px.pie(
    initial_data, names='Do you use environmentally friendly pest and disease-management methods?',
    title='Initial Data: Environmentally Friendly Pest Management',
    color_discrete_sequence=['yellowgreen', 'green']
)

# Boxplots for Initial Data
fig_initial_annual_income = px.box(
    initial_data, y='Annual Income',
    title='Initial Data: Annual Income Distribution',
    color_discrete_sequence=['green'],
    labels={'value': 'Annual Income (UGX)'}
)

fig_initial_cultivated_land = px.box(
    initial_data, y='Area of Cultivated Land',
    title='Initial Data: Area of Cultivated Land Distribution',
    color_discrete_sequence=['yellowgreen'],
    labels={'value': 'Area of Cultivated Land (acres)'},
    range_y = [1,20]
)

fig_initial_production_size = px.box(
    initial_data, y=' Size of Production Cultivated',
    title='Initial Data: Size of Production Cultivated',
    color_discrete_sequence=['mediumseagreen'],
    labels={'value': 'Size of Production Cultivated (kg)'}
)
