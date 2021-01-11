all:

fixlinks:
	find . -name "*.md" -newer .fixlinks -exec ./org-roam-links '{}' \;
	touch .fixlinks

clean:
	find . -name "*~" -delete
