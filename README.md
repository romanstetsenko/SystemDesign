# System Design Documentation

A collection of comprehensive system design guides with interactive diagrams and syntax highlighting.

## ⚙️ Setup Instructions

### Local Usage
1. Clone the repository
2. Open `index.html` in your web browser
3. Click on any document link to view

### Viewing Diagrams
- Mermaid diagrams are embedded in HTML files
- They render automatically when opened in a browser
- For static viewing, use the HTML files directly

### Markdown Files
- Each document has both HTML and Markdown versions
- Markdown files can be viewed directly on GitHub
- HTML files provide interactive diagrams and syntax highlighting

## 🌐 Deployed Applications

**Live Demo:** [https://effective-seagull.static.domains/](https://effective-seagull.static.domains/)

Access all documentation with interactive diagrams and syntax highlighting in a live web environment.

## 📖 Available Documents

**Table of Contents:**
- [1. Notification Service System Design](#1-notification-service-system-design)
- [2. URL Shortener System Design](#2-url-shortener-system-design)
- [3. Rate Limiter Implementation](#3-rate-limiter-implementation)
- [4. System Design Principles](#4-system-design-principles)
 - [5. Top-K System Design](#5-top-k-system-design)

---

### 1. Notification Service System Design
**HTML:** [View with diagrams](notification-service-system-design.html) | **Markdown:** [View source](notification-service-system-design.md)

Complete guide to building scalable notification systems with multi-channel delivery:
- Event-driven architecture
- Multi-channel delivery (push, SMS, email, in-app)
- Fault tolerance and reliability patterns
- User preferences and personalization
- Scalability and performance optimization

### 2. URL Shortener System Design
**HTML:** [View with diagrams](url-shortener-system-design.html) | **Markdown:** [View source](url-shortener-system-design.md)

A complete design for a scalable URL shortening service including:
- Database schema design
- API endpoint specifications
- Load balancing strategies
- Caching mechanisms
- Mermaid architecture diagrams

### 3. Rate Limiter Implementation
**HTML:** [View with diagrams](rate-limiter.html) | **Markdown:** [View source](rate-limiter.md)

Detailed guide on implementing rate limiting algorithms:
- Token Bucket algorithm
- Leaky Bucket algorithm
- Fixed Window counters
- Sliding Window log
- Distributed rate limiting

### 4. System Design Principles
**HTML:** [View with diagrams](system-design-principles.html) | **Markdown:** [View source](system-design-principles.md)

Essential principles for designing scalable systems:
- CAP theorem
- Consistency patterns
- Availability patterns
- Sharding strategies
- Replication methods

### 5. Top-K System Design
**HTML:** [View with diagrams](top-k-system-design.html) | **Markdown:** [View source](top-k-system-design.md)

Compact guide for maintaining top-K items at scale (sharding, sketches, aggregation, merge strategies).

## 🚀 Quick Access

**HTML Files (with interactive diagrams):**
- Main Index: `index.html`
- Notification Service: `notification-service-system-design.html`
- URL Shortener: `url-shortener-system-design.html`
- Rate Limiter: `rate-limiter.html`
- Principles: `system-design-principles.html`
- Top-K: `top-k-system-design.html`

**Markdown Files (for GitHub viewing):**
- Notification Service: `notification-service-system-design.md`
- URL Shortener: `url-shortener-system-design.md`
- Rate Limiter: `rate-limiter.md`
- Principles: `system-design-principles.md`
- Top-K: `top-k-system-design.md`

## ⚡ Features

- ✅ **Interactive Mermaid Diagrams** - Visual architecture representations
- ✅ **Syntax Highlighting** - Clean code blocks with GitHub-style formatting
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Print-Friendly** - Optimized CSS for printing to PDF
- ✅ **Fast Loading** - All dependencies loaded from CDN

## 📁 Repository Structure

```
SystemDesign/
├── notification-service-system-design.html
├── notification-service-system-design.md
├── url-shortener-system-design.html
├── url-shortener-system-design.md
├── rate-limiter.html
├── rate-limiter.md
├── system-design-principles.html
├── system-design-principles.md
├── top-k-system-design.html
├── top-k-system-design.md
├── index.html                   # Main landing page
├── README.md
├── pdf-conversion.md            # PDF conversion guide
├── convert_to_pdf.py            # Python conversion script
├── convert_to_pdf.bat           # Windows batch script
```

## 🔧 Customization

### Add New Documents
1. Create both HTML and Markdown versions of your document
2. Update `index.html` with a new card in the `.card-grid` section
3. Update `README.md` with the new document entry
4. Open `index.html` in a browser to verify

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
