---
# Leave the homepage title empty to use the site title
title: ""
summary: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      ### Choose a user profile to display (a folder name within `content/authors/`)
      username: dharma
      text: ""
      ## Show a call-to-action button under your biography? (optional)
      # button:
      #   text: Download CV
      #   url: uploads/resume.pdf
      headings:
        about: ""
        education: ""
        interests: ""
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true
      # css_class: hbx-bg-gradient
      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      ### Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
      # background:
      #   color: black
      #   image:
      #     # Add your image background to `assets/media/`.
      #     filename: stacked-peaks.svg
      #     filters:
      #       brightness: 1.0
      #     size: cover
      #     position: center
      #     parallax: true
  # - block: markdown
  #   content:
  #     # title: '📚 My Research'
  #     title: '📚 My Research'
  #     subtitle: ''
  #     text: |-
  #       Use this area to speak to your mission. I'm a research scientist in the Moonshot team at DeepMind. I blog about machine learning, deep learning, and moonshots.

  #       I apply a range of qualitative and quantitative methods to comprehensively investigate the role of science and technology in the economy.

  #       Please reach out to collaborate 😃
  #   design:
  #     columns: '1'
  - block: collection
    id: news
    content:
      title: Последние записи
      subtitle: ""
      text: ""
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      ## Choose a layout view
      # view: date-title-summary
      view: card
      # view: article-grid
      # fill_image: false
      columns: "1"
      ## Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  # - block: collection
  #   id: papers
  #   content:
  #     # title: Featured Publications
  #     title: Избранные публикации
  #     filters:
  #       folders:
  #         - publications
  #       featured_only: true
  #   design:
  #     view: article-grid
  #     columns: 2
  - block: collection
    id: papers
    content:
      # title: Recent Publications
      title: Публикации
      text: ""
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      # title: Recent & Upcoming Talks
      title: Выступления
      filters:
        folders:
          - events
    design:
      view: article-grid
      columns: 1
---
<!-- Local Variables: -->
<!-- mode: yaml -->
<!-- End: -->
