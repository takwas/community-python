from ..blueprint import admin
from models import Location, Module_Location
from flask import render_template, url_for, redirect, request, flash


@admin.route('/locations')
def locations():
    locs = Location.select().order_by(Location.available_from)
    return render_template('locations/index.html', locations=locs, Module_Location=Module_Location)


@admin.route('/locations/location/<location_id>')
def location(location_id):
    loc = Location.select().where(Location.id == location_id)

    if not loc.exists():
        flash('Locatie bestaat niet.')
        return redirect(url_for('admin.locations'))

    loc = loc.get()

    return render_template('locations/location.html', location=loc)


@admin.route('/location/new', methods=['POST'])
def new_location():
    city = request.form['city']
    address = request.form['address']
    available_from = request.form['available_from']
    unavailable_from = None if not request.form['unavailable_from'] else request.form['unavailable_from']

    if not city or not address or not available_from:
        flash('Verplichte velden niet ingevuld.')
        return redirect(url_for('admin.locations'))

    newloc = Location(
        city=city,
        address=address,
        available_from=available_from,
        unavailable_from=unavailable_from
    )
    newloc.save()

    return redirect(url_for('admin.locations'))
