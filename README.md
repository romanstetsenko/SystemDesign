# System Design Documentation

A collection of comprehensive system design guides with interactive diagrams and syntax highlighting.

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

**Direct Links:**
- Main Index: `index.html`
- Notification Service: `notification-service-system-design.html`
- URL Shortener: `url-shortener-system-design.html`
- Rate Limiter: `rate-limiter.html`
- Principles: `system-design-principles.html`

## ⚡ Features

- ✅ **Interactive Mermaid Diagrams** - Visual architecture representations
- ✅ **Syntax Highlighting** - Clean code blocks with GitHub-style formatting
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Print-Friendly** - Optimized CSS for printing to PDF
- ✅ **Fast Loading** - All dependencies loaded from CDN

## 🛠️ Setup Instructions

### Local Usage
1. Clone the repository
2. Open `index.html` in your web browser
3. Click on any document link to view

### Viewing Diagrams
- Mermaid diagrams are embedded in HTML files
- They render automatically when opened in a browser
- For static viewing, use the HTML files directly

## 📁 Repository Structure

```
SystemDesign/
├── notification-service-system-design.html
├── url-shortener-system-design.html
├── rate-limiter.html
├── system-design-principles.html
├── index.html                   # Main landing page
├── README.md
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
3. Open `index.html` in a browser to verify

## 🐛 Troubleshooting

### Diagrams Not Rendering?
- Ensure Mermaid CDN links are present in your HTML `<head>`
- Check browser console for any network errors
- Verify the Mermaid script is loading correctly

### Page Shows Raw HTML?
- Open the HTML file directly in a browser (not as raw text)
- Ensure you're viewing the file locally, not through a text editor

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

**Built with ❤️ using Mermaid and Highlight.js**
