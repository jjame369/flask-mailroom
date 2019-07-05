import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all_donations'))


@app.route('/donations')
def all_donations():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        # donation = Donation(donor=request.form['donorname'], value=request.form['donation'])
        rqform = request.form['donorname']
        if rqform.lower() == 'bob':
            doname = '2'
        elif rqform.lower() == 'alice':
            doname = '1'
        elif rqform.lower() == 'charlie':
            doname = '3'
        else:
            doname = '1'
        donation = Donation(donor=doname, value=request.form['donation'])
        donation.save()

        return redirect(url_for('all_donations'))
    else:
        return render_template('newdonations.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

#  <label for="Donor-input">Donor Name:</label><input id="donor-input" type="text" donorname="donorname">
#     <input type="submit" value="Submit Donor Name">