# NIH GRANTS & FUNDINGS DATA
(PIC16B Project - marlene, sharon, skylar, kara)

Read the final post [here](https://linnilinnil.github.io/NIH-Fundings-Dashboard/).

Inspired by the comments from [this NIH blog](https://nexus.od.nih.gov/all/2022/01/18/inequalities-in-the-distribution-of-national-institutes-of-health-research-project-grant-funding/), we build a dashboard based on the NIH research project grants & fundings data to address some questions asked by health science researchers regarding the resource distribution.   

To run the dashboard locally:

We suggest that you create a separate virtual environment running Python 3 for this app, and install all of the required dependencies there.


Run in Terminal/Command Prompt:
<br>
1. Clone the project

`git clone -b main https://github.com/linnilinnil/NIH-Fundings-Dashboard.git`

2. Enter the directory:

`cd NIH-Fundings-Dashboard`

3. Create virtual environment

`python3 -m virtualenv venv`

In UNIX system:

`source venv/bin/activate`

In Windows:

`venv\Scripts\activate`


4. To install all of the required packages to this environment, simply run:

`pip install -r requirements.txt`


5. Lunch the dashboard

Running the *app.py* file directly:

`python3 app.py`  

*(README Reference: Ploly Dash Sample)*
