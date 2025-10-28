from flask import render_template, request, flash, redirect, url_for
from sqlalchemy import or_
from app import app, db
from app.models import Contact, Tag

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search', '')
    if request.method == 'POST' and search_query:
        search_term = f"%{search_query}%"
        contacts = Contact.query.filter(
            or_(
                Contact.fio.ilike(search_term),
                Contact.telephone.ilike(search_term),
                Contact.telegram.ilike(search_term),
                Contact.tags.any(Tag.name.ilike(search_term))
            )
        ).order_by(Contact.fio).all()
    else:
        contacts = Contact.query.order_by(Contact.fio).all()
    
    return render_template('index.html', contacts=contacts, search_query=search_query)

@app.route('/add', methods=['POST'])
def add_contact():
    fio = request.form.get('fio')
    telephone = request.form.get('telephone')
    telegram = request.form.get('telegram')
    tags_str = request.form.get('tags')

    if not Contact.validate_phone(telephone):
        flash('Неверный формат телефона! (Пример: +79991234567)', 'error')
        return redirect(url_for('index'))
    if not Contact.validate_telegram(telegram):
        flash('Неверный формат Telegram! (Пример: @username)', 'error')
        return redirect(url_for('index'))
    
    new_contact = Contact(fio=fio, telephone=telephone, telegram=telegram)

    if tags_str:
        tag_names = [tag.strip().lower() for tag in tags_str.split(',') if tag.strip()]
        for tag_name in tag_names:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
            new_contact.tags.append(tag)

    db.session.add(new_contact)
    db.session.commit()
    flash('Контакт успешно добавлен!', 'success')
    
    return redirect(url_for('index'))