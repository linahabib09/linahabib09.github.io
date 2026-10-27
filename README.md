# Lina Habib — Mechanical Engineering Portfolio

Static multi-page website for GitHub Pages. No build tools required.

## Pages
- `index.html`: Home, project cards, clickable project timeline, contact
- `about.html`: About, skills, academic recognition
- `experience.html`: Education and work experience
- `projects/*.html`: Five project write-ups with media slideshows
- `assets/Lina_Habib_Resume.pdf`: Resume PDF

## Add project media (photos, videos, PDFs)
1. Place files in `assets/media/gearbox/` (or the matching project folder).
2. Open that folder's `media.json` file and list your files:

```json
{
  "items": [
    {"type": "image", "src": "gearbox-front.jpg", "caption": "Gearbox assembly - front view"},
    {"type": "image", "src": "gearbox-detail.png", "caption": "Dog clutch detail"},
    {"type": "video", "src": "gearbox-motion.mp4", "caption": "Gear engagement demonstration"},
    {"type": "pdf", "src": "gearbox-drawings.pdf", "caption": "Technical drawings"}
  ]
}
```

3. Save and upload both the media files and edited `media.json` to your repository.
4. Slideshow navigation works with arrows, thumbnail controls and left/right arrow keys. Videos use playback controls; PDFs open in an embedded viewer (browser-dependent).
5. The first **image** automatically becomes the corresponding project-card and timeline thumbnail. Choose your preferred cover photo as the first image in the list.
6. Until project photos are added, the homepage/timeline use neutral technical illustrations and project pages show an empty gallery. Illustrations are not represented as project photographs.

**Important:** The slideshow fetches `media.json`, so test it via a local web server (e.g. VS Code Live Server or `python -m http.server 8000`) instead of double-clicking `index.html` as a file. GitHub Pages works automatically.

## Edit website
- Main text: edit relevant HTML page.
- Colors, layout and typography: `styles.css` (red variables in final override block).
- Gallery behaviour: `script.js`.
- Source portfolio folder is linked via 'Media archive' in top navigation.
- Project descriptions are based on the provided resume. Replace descriptions with validated results as they develop.

## Publish on GitHub Pages
Upload the *contents* of this folder to your repo root (including `media.json` files), then go to **Settings → Pages**, choose `main` branch, `/(root)`.

The portfolio is a public website, so do not upload confidential drawings, proprietary documents or personally sensitive files.

### StealthComm media (included)
The StealthComm gallery has a compressed 79-second MP4, five original project photos, and a 5-page scrollable PDF. Under the gallery, visitors can open the Python source, full PDF, and original PDF. The first photo is also used as the project thumbnail on the homepage and timeline. To change slide order or captions, edit `assets/media/stealthcomm/media.json`.

### StealthComm slideshow
The slideshow includes photos, a video, a scrollable PDF, scrollable Python code, and an editable PDF download slide. Update `assets/media/stealthcomm/media.json` to reorder items. GitHub Pages or a local web server is needed to load the JSON and code.


## StealthComm gallery local-preview fix
The StealthComm page includes a bundled media manifest as a fallback if the browser blocks JSON fetch on file:// URLs. Actual images, video, PDF and code still require assets/media/stealthcomm/ to remain in place. Publish the entire archive contents at the repo root.


## StealthComm gallery refinement

The image/video stage is centered and uses `object-fit: contain`, so photos are not cropped or stretched. The original landscape MOV has been re-encoded to a high-quality landscape H.264 MP4 rather than the previous low-resolution portrait MP4. Keep `styles.css`, `script.js`, `projects/` and `assets/` at their original relative paths.


New galleries: High Park, AuricleSync documentation, and Classic Tile drawings. Documents are embedded as scrollable PDFs. The source Word and PowerPoint formats were converted to PDF for easier website reading.

### Gallery image zoom
Click a gallery image (or press Enter when focused) to view it enlarged. Press Escape or the × button to close. This does not affect videos or PDFs.

Gearbox Learning Platform is a University of Toronto team project; its project page and homepage description identify the collaborative context.
