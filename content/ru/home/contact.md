---
# an instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Контакты
subtitle:

content:
  # Automatically link email and phone or display as text?
  autolink: true
  
  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

  # Contact details (edit or remove options as required)
  email: 'kulyabov-ds@rudn.ru'
  phone: ''
  address:
    street: ул. Орджоникидзе, 3
    city: г. Москва
    region: Российская Федерация
    postcode: "115419"
    country: Российская Федерация
    country_code: RU

  coordinates:
    latitude: '55.710707'
    longitude: '37.603774'
  directions: Enter Building and take the stairs to Office 384 on Floor 3
  office_hours:
    - 'Monday 09:00 to 16:00'
    - 'Tuesday 09:00 to 16:00'
    - 'Wednesday 09:00 to 16:00'
    - 'Thursday 09:00 to 16:00'
  appointment_url: ''
#  contact_links:
#    - icon: twitter
#      icon_pack: fab
#      name: DM Me
#      link: 'https://twitter.com/Twitter'
#    - icon: video
#      icon_pack: fas
#      name: Zoom Me
#      link: 'https://zoom.com'

design:
  columns: '2'
---
