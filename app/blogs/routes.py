from flask import Blueprint, render_template, abort
from pathlib import Path
import markdown
import frontmatter

blogs_bp = Blueprint("blogs", __name__, url_prefix = "/blogs")

CONTENT_DIR = Path(__file__).resolve().parents[2] / "content" / "blogs"

@blogs_bp.route("/")
def blogs():
    posts = []
    for file in CONTENT_DIR.glob("*.md"):
        post = frontmatter.load(file)
        posts.append({
            "slug": file.stem,
            "title": post.metadata.get("title",file.stem),
            "date": post.metadata.get("date", ""),
            "description": post.metadata.get("description", "")
        })
    return render_template("blogs.html", posts=posts)

@blogs_bp.route("/<slug>")
def blog_detail(slug):
    file = CONTENT_DIR / f"{slug}.md"
    if not file.is_file():
        abort(404)
    post = frontmatter.load(file)
    content = markdown.markdown(
        post.content,
        extensions=["fenced_code", "tables"]
        )
    return render_template(
        "blog_detail.html",
        post=post.metadata,
        content=content
        )