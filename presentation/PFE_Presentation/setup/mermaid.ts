export default () => ({
  theme: 'base',
  themeVariables: {
    primaryColor: '#e8f3f8',
    primaryTextColor: '#03234b',
    primaryBorderColor: '#3cb4e6',
    lineColor: '#03234b',
    secondaryColor: '#fff7cf',
    tertiaryColor: '#ffffff',
    fontFamily: 'Arial, sans-serif',
  },
  themeCSS: ':root { display: block; margin-left: auto; margin-right: auto; }',
  flowchart: {
    useMaxWidth: true,
    htmlLabels: true,
    curve: 'linear',
  },
})
