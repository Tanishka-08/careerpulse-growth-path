/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  darkMode: "class",
  theme: {
    extend: {
      "colors": {
          "tertiary-fixed-dim": "#4edea3",
          "surface-container-high": "#eae7e9",
          "on-secondary-fixed": "#00174b",
          "inverse-on-surface": "#f3f0f2",
          "surface-bright": "#fcf8fa",
          "on-error-container": "#93000a",
          "primary-fixed-dim": "#bec6e0",
          "surface-tint": "#565e74",
          "error-container": "#ffdad6",
          "on-primary-fixed": "#131b2e",
          "surface-container-lowest": "#ffffff",
          "on-tertiary-fixed": "#002113",
          "surface-container-highest": "#e4e2e4",
          "surface-variant": "#e4e2e4",
          "tertiary-fixed": "#6ffbbe",
          "tertiary": "#000000",
          "primary": "#000000",
          "background": "#fcf8fa",
          "on-error": "#ffffff",
          "inverse-surface": "#303032",
          "on-secondary-fixed-variant": "#003ea8",
          "on-surface": "#1b1b1d",
          "surface-dim": "#dcd9db",
          "secondary-container": "#316bf3",
          "inverse-primary": "#bec6e0",
          "outline-variant": "#c6c6cd",
          "on-tertiary-fixed-variant": "#005236",
          "on-tertiary-container": "#009668",
          "secondary-fixed": "#dbe1ff",
          "on-secondary": "#ffffff",
          "on-tertiary": "#ffffff",
          "surface-container": "#f0edef",
          "on-background": "#1b1b1d",
          "on-secondary-container": "#fefcff",
          "on-primary": "#ffffff",
          "primary-container": "#131b2e",
          "surface": "#fcf8fa",
          "on-primary-fixed-variant": "#3f465c",
          "tertiary-container": "#002113",
          "error": "#ba1a1a",
          "secondary": "#0051d5",
          "outline": "#76777d",
          "primary-fixed": "#dae2fd",
          "surface-container-low": "#f6f3f5",
          "on-primary-container": "#7c839b",
          "secondary-fixed-dim": "#b4c5ff",
          "on-surface-variant": "#45464d"
      },
      "fontFamily": {
          "h1": ["Inter"],
          "label-caps": ["Inter"],
          "body-md": ["Inter"],
          "body-lg": ["Inter"],
          "h3": ["Inter"],
          "h2": ["Inter"],
          "stat-number": ["Inter"]
      }
    }
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/container-queries")
  ]
}
