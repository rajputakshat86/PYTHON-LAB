"""
Local Food & Street Vendor Health & Hygiene Rating System
B.Tech. CSEG1021 - Python Programming Project
Uses: Tkinter (GUI), Pandas (Data), Matplotlib (Visualization), NumPy (Numerics), MongoDB (Database)
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
from pymongo import MongoClient
from datetime import datetime
import random

# ─────────────────────────────────────────────
#  MongoDB Connection
# ─────────────────────────────────────────────
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "vendor_hygiene_db"
COLLECTION_NAME = "vendors"

def get_db():
    """Return MongoDB collection. Raises ConnectionError if unavailable."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    client.server_info()  # triggers exception if unreachable
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

# ─────────────────────────────────────────────
#  Rating Logic (NumPy-based)
# ─────────────────────────────────────────────
HYGIENE_CRITERIA = {
    "Personal Hygiene":         {"weight": 0.20, "max": 10},
    "Food Handling Practices":  {"weight": 0.25, "max": 10},
    "Vending Area Cleanliness": {"weight": 0.20, "max": 10},
    "Water & Waste Management": {"weight": 0.15, "max": 10},
    "Food Storage & Temp":      {"weight": 0.10, "max": 10},
    "Pest Control":             {"weight": 0.10, "max": 10},
}

RATING_BANDS = [
    (90, 100, "A+", "#27ae60"),
    (75,  90, "A",  "#2ecc71"),
    (60,  75, "B",  "#f1c40f"),
    (45,  60, "C",  "#e67e22"),
    (30,  45, "D",  "#e74c3c"),
    ( 0,  30, "F",  "#c0392b"),
]

def compute_score(scores: dict) -> float:
    """Weighted average score (0–100) using NumPy."""
    weights = np.array([HYGIENE_CRITERIA[k]["weight"] for k in scores])
    values  = np.array([scores[k] for k in scores])
    maxes   = np.array([HYGIENE_CRITERIA[k]["max"]    for k in scores])
    normalised = (values / maxes) * 100
    return float(np.dot(weights, normalised))

def score_to_grade(score: float):
    for lo, hi, grade, color in RATING_BANDS:
        if lo <= score <= hi:
            return grade, color
    return "F", "#c0392b"

# ─────────────────────────────────────────────
#  Sample Data Seed
# ─────────────────────────────────────────────
SAMPLE_VENDORS = [
    ("Ramesh Chaat Corner",   "Paltan Bazaar",     "Chaat",       {"Personal Hygiene":8,"Food Handling Practices":7,"Vending Area Cleanliness":6,"Water & Waste Management":8,"Food Storage & Temp":7,"Pest Control":9}),
    ("Mohan Samosa Stall",    "Rajpur Road",       "Snacks",      {"Personal Hygiene":5,"Food Handling Practices":6,"Vending Area Cleanliness":4,"Water & Waste Management":5,"Food Storage & Temp":6,"Pest Control":5}),
    ("Priya Juice Centre",    "Clock Tower",       "Beverages",   {"Personal Hygiene":9,"Food Handling Practices":9,"Vending Area Cleanliness":9,"Water & Waste Management":8,"Food Storage & Temp":9,"Pest Control":10}),
    ("Hari Om Dosa Point",    "Parade Ground",     "South Indian",{"Personal Hygiene":3,"Food Handling Practices":4,"Vending Area Cleanliness":3,"Water & Waste Management":2,"Food Storage & Temp":4,"Pest Control":3}),
    ("Quick Bite Noodles",    "Rispana Market",    "Chinese",     {"Personal Hygiene":7,"Food Handling Practices":8,"Vending Area Cleanliness":7,"Water & Waste Management":7,"Food Storage & Temp":8,"Pest Control":7}),
    ("Sonu Pav Bhaji",        "Survey Chowk",      "Street Food", {"Personal Hygiene":6,"Food Handling Practices":6,"Vending Area Cleanliness":5,"Water & Waste Management":6,"Food Storage & Temp":5,"Pest Control":6}),
    ("Geeta Fruit Cart",      "Gandhi Road",       "Fruits",      {"Personal Hygiene":10,"Food Handling Practices":10,"Vending Area Cleanliness":10,"Water & Waste Management":9,"Food Storage & Temp":10,"Pest Control":10}),
    ("Raju Biryani Stall",    "Saharanpur Road",   "Biryani",     {"Personal Hygiene":4,"Food Handling Practices":5,"Vending Area Cleanliness":4,"Water & Waste Management":3,"Food Storage & Temp":4,"Pest Control":4}),
]

# ─────────────────────────────────────────────
#  Main Application
# ─────────────────────────────────────────────
class VendorHygieneApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🍽️  Local Food & Street Vendor Hygiene Rating System")
        self.geometry("1200x750")
        self.configure(bg="#1a1a2e")
        self.resizable(True, True)

        # Try MongoDB; fall back to in-memory list
        try:
            self.collection = get_db()
            self.use_mongo = True
            self._seed_sample_data()
        except Exception:
            self.use_mongo = False
            self.in_memory: list[dict] = []
            self._seed_sample_data_inmem()
            messagebox.showwarning(
                "MongoDB Unavailable",
                "MongoDB is not running.\nUsing in-memory storage instead.\nData will be lost on exit."
            )

        self._build_ui()
        self.refresh_vendor_list()

    # ── Seeding ──────────────────────────────
    def _seed_sample_data(self):
        if self.collection.count_documents({}) == 0:
            for name, location, food_type, scores in SAMPLE_VENDORS:
                self._save_vendor(name, location, food_type, scores)

    def _seed_sample_data_inmem(self):
        for name, location, food_type, scores in SAMPLE_VENDORS:
            score = compute_score(scores)
            grade, _ = score_to_grade(score)
            self.in_memory.append({
                "name": name, "location": location,
                "food_type": food_type, "scores": scores,
                "total_score": round(score, 2), "grade": grade,
                "last_inspected": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })

    # ── UI Construction ──────────────────────
    def _build_ui(self):
        # Title bar
        title_frame = tk.Frame(self, bg="#16213e", pady=10)
        title_frame.pack(fill="x")
        tk.Label(
            title_frame,
            text="🍽️  Local Food & Street Vendor  |  Health & Hygiene Rating System",
            font=("Helvetica", 18, "bold"), fg="#e94560", bg="#16213e"
        ).pack()
        tk.Label(
            title_frame,
            text="B.Tech CSEG1021 — Python Programming Project",
            font=("Helvetica", 10), fg="#a0a0b0", bg="#16213e"
        ).pack()

        # Notebook tabs
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TNotebook",       background="#1a1a2e", borderwidth=0)
        style.configure("TNotebook.Tab",   background="#16213e", foreground="#a0a0b0",
                        padding=[15, 6], font=("Helvetica", 10, "bold"))
        style.map("TNotebook.Tab", background=[("selected", "#e94560")],
                  foreground=[("selected", "white")])

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=10, pady=5)

        self.tab_dashboard  = tk.Frame(nb, bg="#1a1a2e")
        self.tab_add        = tk.Frame(nb, bg="#1a1a2e")
        self.tab_analytics  = tk.Frame(nb, bg="#1a1a2e")
        self.tab_search     = tk.Frame(nb, bg="#1a1a2e")

        nb.add(self.tab_dashboard, text="📋  Dashboard")
        nb.add(self.tab_add,       text="➕  Add Vendor")
        nb.add(self.tab_analytics, text="📊  Analytics")
        nb.add(self.tab_search,    text="🔍  Search")

        self._build_dashboard()
        self._build_add_vendor()
        self._build_analytics()
        self._build_search()

    # ── Tab 1: Dashboard ─────────────────────
    def _build_dashboard(self):
        top = tk.Frame(self.tab_dashboard, bg="#1a1a2e")
        top.pack(fill="x", padx=15, pady=8)

        tk.Label(top, text="All Registered Vendors", font=("Helvetica", 13, "bold"),
                 fg="white", bg="#1a1a2e").pack(side="left")

        btn_frame = tk.Frame(top, bg="#1a1a2e")
        btn_frame.pack(side="right")
        self._btn(btn_frame, "🔄 Refresh",     self.refresh_vendor_list, "#0f3460").pack(side="left", padx=4)
        self._btn(btn_frame, "🗑️  Delete",     self._delete_selected,    "#e94560").pack(side="left", padx=4)
        self._btn(btn_frame, "📊 View Charts", self._show_selected_chart,"#533483").pack(side="left", padx=4)

        cols = ("Vendor Name", "Location", "Food Type", "Score", "Grade", "Last Inspected")
        self.tree = ttk.Treeview(self.tab_dashboard, columns=cols, show="headings", height=20)
        widths    = [200, 160, 120, 80, 70, 160]
        for col, w in zip(cols, widths):
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, width=w, anchor="center")

        style = ttk.Style()
        style.configure("Treeview",
            background="#0f3460", foreground="white", fieldbackground="#0f3460",
            rowheight=28, font=("Helvetica", 10))
        style.configure("Treeview.Heading",
            background="#16213e", foreground="#e94560",
            font=("Helvetica", 10, "bold"))
        style.map("Treeview", background=[("selected", "#e94560")])

        self.tree.tag_configure("good",    background="#1a4731")
        self.tree.tag_configure("average", background="#3d3000")
        self.tree.tag_configure("poor",    background="#4d1010")

        sb = ttk.Scrollbar(self.tab_dashboard, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(15, 0), pady=5)
        sb.pack(side="left", fill="y", pady=5)

    # ── Tab 2: Add Vendor ────────────────────
    def _build_add_vendor(self):
        canvas = tk.Canvas(self.tab_add, bg="#1a1a2e", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        frame = tk.Frame(canvas, bg="#1a1a2e")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        tk.Label(frame, text="Register New Vendor", font=("Helvetica", 14, "bold"),
                 fg="#e94560", bg="#1a1a2e").grid(row=0, column=0, columnspan=2,
                                                   pady=(15, 10), padx=20)

        # Basic info
        fields = [("Vendor / Stall Name *", "entry"), ("Location / Area *", "entry"),
                  ("Food Type / Category", "entry")]
        self.add_vars = {}
        for i, (label, _) in enumerate(fields, start=1):
            tk.Label(frame, text=label, font=("Helvetica", 10), fg="#a0a0b0",
                     bg="#1a1a2e").grid(row=i, column=0, sticky="e", padx=(20, 8), pady=6)
            var = tk.StringVar()
            tk.Entry(frame, textvariable=var, width=30, bg="#0f3460", fg="white",
                     insertbackground="white", font=("Helvetica", 10),
                     relief="flat", bd=4).grid(row=i, column=1, sticky="w", pady=6)
            key = label.replace(" *", "").strip().lower().replace(" / ", "_").replace(" ", "_")
            self.add_vars[key] = var

        # Score sliders
        tk.Label(frame, text="Hygiene Scores  (0 = very poor  →  10 = excellent)",
                 font=("Helvetica", 11, "bold"), fg="white",
                 bg="#1a1a2e").grid(row=4, column=0, columnspan=2, pady=(18, 6))

        self.score_vars = {}
        for i, (criterion, info) in enumerate(HYGIENE_CRITERIA.items()):
            row = 5 + i
            wt_pct = int(info["weight"] * 100)
            tk.Label(frame, text=f"{criterion}  ({wt_pct}% weight)",
                     font=("Helvetica", 10), fg="#a0a0b0",
                     bg="#1a1a2e").grid(row=row, column=0, sticky="e", padx=(20, 8), pady=5)
            sv = tk.IntVar(value=5)
            sl = tk.Scale(frame, from_=0, to=10, orient="horizontal", variable=sv,
                          length=220, bg="#0f3460", fg="white", troughcolor="#16213e",
                          highlightthickness=0, activebackground="#e94560",
                          font=("Helvetica", 9))
            sl.grid(row=row, column=1, sticky="w", pady=5)
            self.score_vars[criterion] = sv

        # Live score preview
        self.live_score_label = tk.Label(frame, text="Estimated Score: —",
                                          font=("Helvetica", 12, "bold"),
                                          fg="#f1c40f", bg="#1a1a2e")
        self.live_score_label.grid(row=11, column=0, columnspan=2, pady=8)
        for sv in self.score_vars.values():
            sv.trace_add("write", self._update_live_score)

        btn_row = tk.Frame(frame, bg="#1a1a2e")
        btn_row.grid(row=12, column=0, columnspan=2, pady=14)
        self._btn(btn_row, "💾  Save Vendor",  self._save_new_vendor,  "#27ae60", width=18).pack(side="left", padx=8)
        self._btn(btn_row, "🔄  Clear Form",   self._clear_add_form,   "#7f8c8d", width=14).pack(side="left", padx=8)

    def _update_live_score(self, *_):
        scores = {k: v.get() for k, v in self.score_vars.items()}
        sc = compute_score(scores)
        grade, color = score_to_grade(sc)
        self.live_score_label.config(
            text=f"Estimated Score: {sc:.1f} / 100   ➜   Grade: {grade}",
            fg=color
        )

    # ── Tab 3: Analytics ─────────────────────
    def _build_analytics(self):
        btn_row = tk.Frame(self.tab_analytics, bg="#1a1a2e")
        btn_row.pack(fill="x", padx=15, pady=8)
        self._btn(btn_row, "📊 Grade Distribution",   self._chart_grade_dist,    "#0f3460").pack(side="left", padx=5)
        self._btn(btn_row, "📈 Score Comparison",     self._chart_score_compare, "#533483").pack(side="left", padx=5)
        self._btn(btn_row, "🥧 Food Type Breakdown",  self._chart_food_type,     "#e94560").pack(side="left", padx=5)
        self._btn(btn_row, "📉 Criteria Heatmap",     self._chart_heatmap,       "#16a085").pack(side="left", padx=5)

        self.analytics_frame = tk.Frame(self.tab_analytics, bg="#1a1a2e")
        self.analytics_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # ── Tab 4: Search ────────────────────────
    def _build_search(self):
        top = tk.Frame(self.tab_search, bg="#1a1a2e")
        top.pack(fill="x", padx=15, pady=10)
        tk.Label(top, text="🔍  Search Vendor:", font=("Helvetica", 11),
                 fg="white", bg="#1a1a2e").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._do_search)
        tk.Entry(top, textvariable=self.search_var, width=35,
                 bg="#0f3460", fg="white", insertbackground="white",
                 font=("Helvetica", 11), relief="flat", bd=5).pack(side="left", padx=10)

        cols = ("Vendor Name", "Location", "Food Type", "Score", "Grade")
        self.search_tree = ttk.Treeview(self.tab_search, columns=cols,
                                         show="headings", height=22)
        for col in cols:
            self.search_tree.heading(col, text=col, anchor="center")
            self.search_tree.column(col, width=200, anchor="center")
        self.search_tree.pack(fill="both", expand=True, padx=15, pady=5)

    # ── Data Layer ───────────────────────────
    def _save_vendor(self, name, location, food_type, scores):
        score = compute_score(scores)
        grade, _ = score_to_grade(score)
        record = {
            "name": name, "location": location, "food_type": food_type,
            "scores": scores, "total_score": round(score, 2), "grade": grade,
            "last_inspected": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        if self.use_mongo:
            self.collection.insert_one(record)
        else:
            self.in_memory.append(record)

    def _all_vendors(self) -> list[dict]:
        if self.use_mongo:
            return list(self.collection.find({}, {"_id": 0}))
        return list(self.in_memory)

    def _vendors_df(self) -> pd.DataFrame:
        return pd.DataFrame(self._all_vendors())

    # ── Dashboard Actions ────────────────────
    def refresh_vendor_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        vendors = self._all_vendors()
        vendors_sorted = sorted(vendors, key=lambda v: v.get("total_score", 0), reverse=True)
        for v in vendors_sorted:
            score = v.get("total_score", 0)
            tag = "good" if score >= 75 else ("average" if score >= 50 else "poor")
            self.tree.insert("", "end",
                values=(v["name"], v["location"], v.get("food_type", "N/A"),
                        f"{score:.1f}", v["grade"], v["last_inspected"]),
                tags=(tag,))

    def _delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a vendor to delete.")
            return
        item = self.tree.item(sel[0])["values"]
        name = item[0]
        if messagebox.askyesno("Confirm Delete", f"Delete '{name}'?"):
            if self.use_mongo:
                self.collection.delete_one({"name": name})
            else:
                self.in_memory = [v for v in self.in_memory if v["name"] != name]
            self.refresh_vendor_list()

    def _show_selected_chart(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a vendor.")
            return
        name = self.tree.item(sel[0])["values"][0]
        vendors = self._all_vendors()
        vendor = next((v for v in vendors if v["name"] == name), None)
        if not vendor:
            return
        scores = vendor["scores"]
        criteria = list(scores.keys())
        values   = [scores[c] for c in criteria]
        short    = [c.split()[0] for c in criteria]

        fig, ax = plt.subplots(figsize=(7, 4), facecolor="#1a1a2e")
        ax.set_facecolor("#0f3460")
        bars = ax.bar(short, values, color=["#e94560","#f39c12","#27ae60",
                                             "#3498db","#9b59b6","#1abc9c"],
                      edgecolor="white", linewidth=0.5)
        ax.set_ylim(0, 10)
        ax.set_title(f"{name} — Hygiene Breakdown", color="white", fontsize=12, fontweight="bold")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                    str(val), ha="center", va="bottom", color="white", fontsize=9)
        win = tk.Toplevel(self)
        win.title(f"Hygiene Chart — {name}")
        win.configure(bg="#1a1a2e")
        FigureCanvasTkAgg(fig, master=win).get_tk_widget().pack(fill="both", expand=True)

    # ── Add Vendor Actions ───────────────────
    def _save_new_vendor(self):
        name      = self.add_vars["vendor_/_stall_name"].get().strip()
        location  = self.add_vars["location_/_area"].get().strip()
        food_type = self.add_vars["food_type_/_category"].get().strip() or "General"
        if not name or not location:
            messagebox.showerror("Missing Info", "Vendor Name and Location are required.")
            return
        scores = {k: v.get() for k, v in self.score_vars.items()}
        self._save_vendor(name, location, food_type, scores)
        score = compute_score(scores)
        grade, _ = score_to_grade(score)
        messagebox.showinfo("Saved ✅",
            f"Vendor '{name}' registered!\nScore: {score:.1f}/100   Grade: {grade}")
        self._clear_add_form()
        self.refresh_vendor_list()

    def _clear_add_form(self):
        for var in self.add_vars.values():
            var.set("")
        for sv in self.score_vars.values():
            sv.set(5)

    # ── Analytics Charts ─────────────────────
    def _clear_analytics(self):
        for w in self.analytics_frame.winfo_children():
            w.destroy()

    def _embed_fig(self, fig):
        self._clear_analytics()
        canvas = FigureCanvasTkAgg(fig, master=self.analytics_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def _chart_grade_dist(self):
        df = self._vendors_df()
        if df.empty:
            messagebox.showinfo("No Data", "No vendors in the system yet.")
            return
        grade_counts = df["grade"].value_counts()
        colors = {"A+": "#27ae60","A": "#2ecc71","B": "#f1c40f",
                  "C": "#e67e22","D": "#e74c3c","F": "#c0392b"}
        fig, ax = plt.subplots(figsize=(7, 5), facecolor="#1a1a2e")
        ax.set_facecolor("#0f3460")
        wedges, texts, autotexts = ax.pie(
            grade_counts.values, labels=grade_counts.index,
            autopct="%1.1f%%", startangle=140,
            colors=[colors.get(g, "#999") for g in grade_counts.index],
            textprops={"color": "white"})
        ax.set_title("Grade Distribution of Vendors", color="white",
                     fontsize=13, fontweight="bold")
        self._embed_fig(fig)

    def _chart_score_compare(self):
        df = self._vendors_df()
        if df.empty:
            return
        df_sorted = df.sort_values("total_score", ascending=True)
        fig, ax = plt.subplots(figsize=(9, max(5, len(df_sorted) * 0.5)), facecolor="#1a1a2e")
        ax.set_facecolor("#0f3460")
        colors = ["#27ae60" if s >= 75 else "#f1c40f" if s >= 50 else "#e74c3c"
                  for s in df_sorted["total_score"]]
        bars = ax.barh(df_sorted["name"], df_sorted["total_score"], color=colors)
        ax.set_xlim(0, 100)
        ax.axvline(75, color="#2ecc71", linestyle="--", alpha=0.6, label="Good (75)")
        ax.axvline(50, color="#e67e22", linestyle="--", alpha=0.6, label="Average (50)")
        ax.set_title("Vendor Hygiene Score Comparison", color="white",
                     fontsize=13, fontweight="bold")
        ax.tick_params(colors="white")
        ax.legend(facecolor="#1a1a2e", labelcolor="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
        for bar, score in zip(bars, df_sorted["total_score"]):
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                    f"{score:.1f}", va="center", color="white", fontsize=8)
        fig.tight_layout()
        self._embed_fig(fig)

    def _chart_food_type(self):
        df = self._vendors_df()
        if df.empty:
            return
        ft_avg = df.groupby("food_type")["total_score"].mean().sort_values()
        fig, ax = plt.subplots(figsize=(8, 5), facecolor="#1a1a2e")
        ax.set_facecolor("#0f3460")
        bars = ax.bar(ft_avg.index, ft_avg.values,
                      color=plt.cm.Set3(np.linspace(0, 1, len(ft_avg))))
        ax.set_ylim(0, 100)
        ax.set_title("Average Hygiene Score by Food Type", color="white",
                     fontsize=13, fontweight="bold")
        ax.set_xlabel("Food Type", color="white")
        ax.set_ylabel("Avg Score", color="white")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#333")
        for bar, val in zip(bars, ft_avg.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                    f"{val:.1f}", ha="center", color="white", fontsize=9)
        fig.tight_layout()
        self._embed_fig(fig)

    def _chart_heatmap(self):
        vendors = self._all_vendors()
        if not vendors:
            return
        rows = []
        for v in vendors:
            row = {"Vendor": v["name"][:18]}
            row.update(v.get("scores", {}))
            rows.append(row)
        df = pd.DataFrame(rows).set_index("Vendor")
        fig, ax = plt.subplots(figsize=(10, max(4, len(df) * 0.5)), facecolor="#1a1a2e")
        im = ax.imshow(df.values, aspect="auto", cmap="RdYlGn", vmin=0, vmax=10)
        ax.set_xticks(range(len(df.columns)))
        ax.set_xticklabels([c.split()[0] for c in df.columns],
                           rotation=30, ha="right", color="white", fontsize=8)
        ax.set_yticks(range(len(df.index)))
        ax.set_yticklabels(df.index, color="white", fontsize=8)
        ax.set_title("Criteria-wise Score Heatmap (0–10)", color="white",
                     fontsize=12, fontweight="bold")
        plt.colorbar(im, ax=ax)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                ax.text(j, i, str(df.values[i, j]), ha="center", va="center",
                        color="white" if df.values[i, j] < 6 else "black", fontsize=8)
        fig.tight_layout()
        self._embed_fig(fig)

    # ── Search ───────────────────────────────
    def _do_search(self, *_):
        query = self.search_var.get().strip().lower()
        for row in self.search_tree.get_children():
            self.search_tree.delete(row)
        for v in self._all_vendors():
            if (query in v["name"].lower() or
                    query in v.get("location", "").lower() or
                    query in v.get("food_type", "").lower()):
                self.search_tree.insert("", "end",
                    values=(v["name"], v["location"], v.get("food_type", "N/A"),
                            f"{v['total_score']:.1f}", v["grade"]))

    # ── Helper ───────────────────────────────
    @staticmethod
    def _btn(parent, text, command, bg, width=14):
        return tk.Button(parent, text=text, command=command, bg=bg, fg="white",
                         font=("Helvetica", 9, "bold"), relief="flat",
                         padx=10, pady=5, cursor="hand2", width=width,
                         activebackground="#e94560", activeforeground="white")


# ─────────────────────────────────────────────
#  Entry Point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = VendorHygieneApp()
    app.mainloop()
