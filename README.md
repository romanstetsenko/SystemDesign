# System Design Documentation

A collection of comprehensive system design guides with interactive diagrams and syntax highlighting, hosted on GitHub Pages.

## 📖 Available Documents

### 1. [Notification Service System Design](notification-service-system-design.html)
Complete guide to building scalable notification systems with multi-channel delivery:
- Event-driven architecture
- Multi-channel delivery (push, SMS, email, in-app)
- Fault tolerance and reliability patterns
- User preferences and personalization
- Scalability and performance optimization

### 2. [URL Shortener System Design](url-shortener-system-design.html)
A complete design for a scalable URL shortening service including:
- Database schema design
- API endpoint specifications
- Load balancing strategies
- Caching mechanisms
- Mermaid architecture diagrams

### 3. [Rate Limiter Implementation](rate-limiter.html)
Detailed guide on implementing rate limiting algorithms:
- Token Bucket algorithm
- Leaky Bucket algorithm
- Fixed Window counters
- Sliding Window log
- Distributed rate limiting

### 4. [System Design Principles](system-design-principles.html)
Essential principles for designing scalable systems:
- CAP theorem
- Consistency patterns
- Availability patterns
- Sharding strategies
- Replication methods

## 🚀 Quick Access

**Direct Links (once GitHub Pages is enabled):**
- Main Index: `https://yourusername.github.io/SystemDesign/`
- Notification Service: `https://yourusername.github.io/SystemDesign/notification-service-system-design.html`
- URL Shortener: `https://yourusername.github.io/SystemDesign/url-shortener-system-design.html`
- Rate Limiter: `https://yourusername.github.io/SystemDesign/rate-limiter.html`
- Principles: `https://yourusername.github.io/SystemDesign/system-design-principles.html`

## ⚡ Features

- ✅ **Interactive Mermaid Diagrams** - Visual architecture representations
- ✅ **Syntax Highlighting** - Clean code blocks with GitHub-style formatting
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Print-Friendly** - Optimized CSS for printing to PDF
- ✅ **Fast Loading** - All dependencies loaded from CDN

## 🛠️ Setup Instructions

### Option 1: Enable GitHub Pages (Recommended)

1. **Go to your repository settings:**
   - Navigate to `Settings` → `Pages`
   - Under "Build and deployment", select `Source`: `Deploy from a branch`
   - Choose `main` or `master` branch
   - Select `/ (root)` folder
   - Click `Save`

2. **Wait for deployment:**
   - GitHub will automatically deploy your site
   - You'll see a green checkmark when deployment is complete
   - Your site will be available at: `https://yourusername.github.io/SystemDesign/`

### Option 2: Use GitHub Actions (Automatic Deployment)

The repository includes a GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) that automatically deploys your site on every push.

1. **Enable GitHub Actions:**
   - Go to `Settings` → `Actions` → `General`
   - Under "Workflow permissions", ensure "Read and write permissions" is selected

2. **Trigger deployment:**
   - Push any changes to your repository
   - Go to `Actions` tab to monitor the deployment
   - Once complete, your site will be live

### Option 3: Manual Setup

If you prefer manual control:

1. **Create a `gh-pages` branch:**
   ```bash
   git checkout --orphan gh-pages
   git rm -rf .
   git add .
   git commit -m "Initial gh-pages commit"
   git push origin gh-pages
   ```

2. **Configure GitHub Pages:**
   - Go to `Settings` → `Pages`
   - Select `gh-pages` branch
   - Click `Save`

## 📁 Repository Structure

```
SystemDesign/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml    # GitHub Actions for auto-deployment
├── notification-service-system-design.html
├── url-shortener-system-design.html
├── rate-limiter.html
├── system-design-principles.html
├── index.html                   # Main landing page
├── README.md
└── .nojekyll                    # Disables Jekyll processing
```

## 🔧 Customization

### Update the GitHub Link
In `index.html`, line 78:
```html
<a href="https://github.com/yourusername/SystemDesign" class="github-link" target="_blank">View on GitHub →</a>
```
Replace `yourusername` with your actual GitHub username.

### Add New Documents
1. Add your HTML file to the repository
2. Update `index.html` with a new card in the `.card-grid` section
3. Push changes - GitHub Pages will auto-deploy

## 🐛 Troubleshooting

### Diagrams Not Rendering?
- Ensure Mermaid CDN links are present in your HTML `<head>`
- Check browser console for any network errors
- Verify the Mermaid script is loading correctly

### Page Shows Raw HTML?
- Make sure `.nojekyll` file exists in the root
- Check that GitHub Pages is configured to deploy from the root directory
- Wait a few minutes for deployment to complete

### Links Not Working?
- Use URL encoding for spaces: `%20` instead of spaces
- Test links locally by opening `index.html` in a browser
- Ensure file names match exactly (case-sensitive)

## 📄 License

These documentation files are provided as-is for educational purposes.

## 🤝 Contributing

Feel free to:
- Add new system design topics
- Improve existing documentation
- Enhance the UI/UX of the landing page
- Add more interactive features

---

**Built with ❤️ using GitHub Pages**
