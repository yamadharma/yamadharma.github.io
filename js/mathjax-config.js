// MathJax Configuration
//
// v2 to v3 upgrade notes:
// - The CommonHTML.linebreaks option is not yet implemented (but may be in a future release)
// - The TeX.noUndefined.attributes option is not yet implemented (but may be in a future release)
window.MathJax = {
    loader: {
	load: ['[tex]/noerrors'],
	load: ['[tex]/newcommand'],
	load: ['[tex]/physics'],
    },
    tex: {
	inlineMath: [
	    ['$', '$'],
	    ['\\(', '\\)'],
	],
	displayMath: [
	    ['$$', '$$'],
	    ['\\[', '\\]'],
	],
	processEscapes: false,
	tags: 'ams',
	packages: {'[+]': ['noerrors']},
	packages: {'[+]': ['newcommand']},
	packages: {'[+]': ['physics']},
	macros: {
	    crd: ["{\\underline {\\vphantom{j} #1}}", 1],
	    ii: ["{\\mathrm{i}}", 1],
	    iiz: ["{\\varepsilon}", 1],
	    iip: ["{\\mathrm{e}}", 1],
	},
    }
};
