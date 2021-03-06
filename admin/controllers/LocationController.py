from helpers.enums import AlertType
from middleware import ValidationMiddleware
from ..blueprint import admin
from models import Location, Module_Location
from flask import render_template, url_for, redirect, request, flash
from datetime import datetime
from helpers import validate


@admin.route('/locations')
def locations():
    locs = Location.select().order_by(Location.available_from)
    return render_template('locations/index.html', locations=locs, Module_Location=Module_Location, datetime=datetime)


@admin.route('/locations/location/<location_uuid>')
@ValidationMiddleware.uuid_validation(redirect_url='admin.locations')
def location(location_uuid):

    loc = Location.select().where(Location.uuid == location_uuid)

    if not loc.exists():
        flash('Locatie bestaat niet.', AlertType.WARNING.value)
        return redirect(url_for('admin.locations'))

    loc = loc.get()

    current_placed_modules = Module_Location.select().where(Module_Location.location == loc).where(Module_Location.start_date <= datetime.now().date()).where(Module_Location.end_date >= datetime.now().date())

    return render_template('locations/location.html', location=loc, current_placed_modules=current_placed_modules)


@admin.route('/location/new', methods=['POST'])
def new_location():
    city = request.form['city']
    address = request.form['address']
    available_from = request.form['available_from']
    unavailable_from = None if not request.form['unavailable_from'] else request.form['unavailable_from']

    if not city or not address or not available_from:
        flash('Verplichte velden niet ingevuld.', AlertType.WARNING.value)
        return redirect(url_for('admin.locations'))

    newloc = Location(
        city=city,
        address=address,
        available_from=available_from,
        unavailable_from=unavailable_from
    )
    newloc.save()

    return redirect(url_for('admin.locations'))
