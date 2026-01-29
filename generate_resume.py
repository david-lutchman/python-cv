from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import date

OUTPUT_PDF = "david-lutchman-2026.pdf"

# -----------------------------
# RESUME CONTENT
# -----------------------------
NAME = "DAVID LUTCHMAN"
LOCATION_LINE = "Maraval, Trinidad & Tobago"
CONTACT_LINE = "(868) 687-6800 | dlutchman@gmail.com | linkedin.com/in/dlutchman"
TITLE = "Network Security / Infrastructure Engineer (Tier 2/3 Support, Hospitality, Retail, Financial Sector)"

SUMMARY = (
    "IT professional with 20+ years of experience across network security and enterprise infrastructure, including "
    "Tier 2/3 technical support in production environments. Specialized in troubleshooting complex, multi-system "
    "incidents across routing/switching, VPNs, wireless, firewalls, endpoint security, virtualization, and backups. "
    "Strong operational discipline in monitoring, documentation, change control, and recovery testing. "
)

SKILLS = [
    "Advanced Troubleshooting (Tier 2/3) | Root Cause Analysis | Incident Response",
    "Networking: TCP/IP, DNS, DHCP, VLANs, NAT, QoS, SD-WAN, Site-to-Site + Remote Access VPN",
    "Firewalls/Security: Check Point (policy/NAT/VPN/threat prevention), FortiGate, F5 VPN, IDS/IPS",
    "Threat Detection & Endpoint: Darktrace, XDR concepts, CrowdStrike (monitoring/triage/response)",
    "Wireless: Aruba, Cisco Meraki, Ubiquiti, Extreme, Ruijie",
    "Virtualization/Infra: Nutanix AHV, VMware, Linux (RHEL)",
    "Backup/DR: HYCU for Nutanix, backup validation, restore testing, retention compliance",
    "Automation: Python scripting, log parsing, API-driven diagnostics; AI-assisted tooling (ChatGPT, Google Gemini)",
    "Tools/ITSM/Monitoring: ManageEngine, Solarwinds, Nagios (and similar monitoring/alerting platforms)",
    "Documentation/Change Control: diagrams, asset inventory, SOPs/runbooks, rollback plans",
]

EXPERIENCE = [
    {
        "company": "HADCO Group",
        "location": "San Juan, Trinidad & Tobago",
        "role": "Network Security Administrator",
        "dates": "Feb 2022 – Present",
        "bullets": [
            "Provide Tier 2/3 support for network, wireless, security, and infrastructure incidents across multi-site environments.",
            "Administer Check Point firewalls: policy changes, NAT, VPNs, and threat-prevention tuning; troubleshoot complex access and connectivity faults.",
            "Monitor and respond to Darktrace alerts; investigate anomalies and coordinate containment/remediation actions with stakeholders and vendors.",
            "Support corporate and hotel property networks, including segmentation for guest, staff, POS, CCTV, and back-office systems.",
            "Support wireless and switching environments (Meraki/Ubiquiti; also Aruba/Extreme/Ruijie where present) with focus on stability and performance.",
            "Administer Nutanix infrastructure (clusters, storage/performance monitoring, VM lifecycle) and support infrastructure migrations.",
            "Operate HYCU backup/DR for Nutanix: job monitoring, verification, restore tests, retention compliance, and procedure documentation.",
            "Maintain documentation: network diagrams, IP allocations, asset inventory, configs; execute change control with validation and rollback planning.",
        ],
    },
    {
        "company": "Value Optical Limited",
        "location": "Chaguanas, Trinidad & Tobago",
        "role": "Senior Systems Administrator",
        "dates": "Nov 2020 – Feb 2022",
        "bullets": [
            "Escalation point for complex infrastructure and network incidents; drove root-cause analysis and resolution under production constraints.",
            "Managed VMware and Cisco network environments; implemented Remote Access VPN, Wi-Fi improvements, WSUS, monitoring, and operational runbooks.",
            "Managed backup and disaster recovery operations; improved readiness via recurring restore testing and failure remediation.",
            "Provided technical leadership to IT Operations team; improved incident handling consistency and documentation quality.",
        ],
    },
    {
        "company": "Celebrity Cruises",
        "location": "Florida, USA",
        "role": "IT Infrastructure Specialist",
        "dates": "Aug 2018 – Mar 2020",
        "bullets": [
            "Provided Tier 1/2 support for shipboard networking, systems, and applications in always-on production environments.",
            "Supported VOIP deployments and troubleshooting; maintained service continuity under strict operational timelines.",
            "Contributed to infrastructure deployment as part of the project team for a new ship build (Edge Class).",
        ],
    },
    {
        "company": "Janouras Custom Design Limited",
        "location": "Port of Spain, Trinidad & Tobago",
        "role": "Systems Administrator",
        "dates": "Oct 2016 – Aug 2018",
        "bullets": [
            "Sole IT resource delivering end-to-end support across networking, security, and systems operations.",
            "Implemented FortiGate UTM and site-to-site VPN connectivity; resolved multi-site connectivity issues and improved uptime.",
            "Deployed and supported CCTV/security systems across branch locations.",
        ],
    },
    {
        "company": "Colonial Fire & General Insurance Co. Ltd (COLFIRE)",
        "location": "Trinidad & Tobago",
        "role": "Network Administrator",
        "dates": "Apr 2012 – Oct 2016",
        "bullets": [
            "Administered Cisco Call Manager, F5 VPN, and Microsoft Exchange; resolved complex connectivity and service issues.",
            "Performed backups of critical financial applications and data; supported inter-branch connectivity for online operations.",
            "Conducted audits to maintain compliance with licensing standards.",
        ],
    },
]

# Hotel property emphasis + Python/AI tooling
PROJECTS = [
    "Hotel Property Network Support: Supported and deployed infrastructure to hotel properties where uptime and guest experience are critical; maintained secure segmentation for guest Wi-Fi, staff, POS, CCTV, and back-office systems.",
    "Hospitality Incident Response: Led troubleshooting for guest-impacting connectivity issues (WAN faults, wireless instability, DNS/DHCP problems), coordinating changes with validation.",
    "Python + AI Diagnostics: Built Python tools using ChatGPT and Google Gemini to automate site health checks, parse logs, and generate standardized incident summaries to speed resolution.",
]

CERTS_EDU = [
    "CISSP Coursework – Elizabeth Sloane Institute of Technology (2023)",
    "Cisco Certified Entry Networking Technician (CCENT) (2015)",
    "Red Hat Linux Enterprise Administration (2013)",
    "Microsoft Certified Systems Engineer (MCSE) (2002)",
    "GCE A Levels – Trinity College Moka, Maraval (2000)",
]

# -----------------------------
# PDF RENDERING HELPERS
# -----------------------------
PAGE_W, PAGE_H = LETTER
MARGIN_L = 0.75 * inch
MARGIN_R = 0.75 * inch
MARGIN_T = 0.75 * inch
MARGIN_B = 0.75 * inch

FONT = "Helvetica"
FONT_B = "Helvetica-Bold"
FONT_SIZE = 10
SECTION_TITLE_SIZE = 11
NAME_SIZE = 16
LINE_GAP = 3

MAX_WIDTH = PAGE_W - MARGIN_L - MARGIN_R

def wrap_text(text, font_name, font_size, max_width):
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = (current + " " + w).strip()
        if stringWidth(test, font_name, font_size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

def draw_lines(c, lines, x, y, font_name=FONT, font_size=FONT_SIZE):
    c.setFont(font_name, font_size)
    lh = font_size + LINE_GAP
    for line in lines:
        c.drawString(x, y, line)
        y -= lh
    return y

def draw_section_header(c, title, y):
    y -= 6
    c.setFont(FONT_B, SECTION_TITLE_SIZE)
    c.drawString(MARGIN_L, y, title.upper())
    y -= (SECTION_TITLE_SIZE + LINE_GAP)
    c.setLineWidth(0.5)
    c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
    y -= 10
    return y

def start_page(c):
    c.setAuthor(NAME)
    c.setTitle(f"{NAME} - Resume")
    return PAGE_H - MARGIN_T

def ensure_space(c, y, needed_lines=3):
    lh = FONT_SIZE + LINE_GAP
    if y - (needed_lines * lh) < MARGIN_B:
        c.showPage()
        return start_page(c)
    return y

# -----------------------------
# BUILD PDF
# -----------------------------
def build_pdf(path):
    c = canvas.Canvas(path, pagesize=LETTER)
    y = start_page(c)

    # Header
    c.setFont(FONT_B, NAME_SIZE)
    c.drawString(MARGIN_L, y, NAME)
    y -= (NAME_SIZE + 6)

    c.setFont(FONT, FONT_SIZE)
    for line in [LOCATION_LINE, CONTACT_LINE, TITLE]:
        y = draw_lines(c, wrap_text(line, FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
    y -= 6

    # Summary
    y = draw_section_header(c, "Professional Summary", y)
    y = ensure_space(c, y, needed_lines=6)
    y = draw_lines(c, wrap_text(SUMMARY, FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
    y -= 6

    # Skills
    y = draw_section_header(c, "Core Skills", y)
    for s in SKILLS:
        y = ensure_space(c, y, needed_lines=2)
        y = draw_lines(c, wrap_text(f"• {s}", FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
    y -= 6

    # Experience
    y = draw_section_header(c, "Professional Experience", y)
    for job in EXPERIENCE:
        y = ensure_space(c, y, needed_lines=5)
        c.setFont(FONT_B, FONT_SIZE)
        c.drawString(MARGIN_L, y, f"{job['role']} | {job['company']}")
        y -= (FONT_SIZE + LINE_GAP)

        c.setFont(FONT, FONT_SIZE)
        y = draw_lines(c, wrap_text(f"{job['location']} | {job['dates']}", FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
        y -= 2

        for b in job["bullets"]:
            y = ensure_space(c, y, needed_lines=2)
            y = draw_lines(c, wrap_text(f"• {b}", FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
        y -= 8

    # Projects
    y = draw_section_header(c, "Selected Projects (Hospitality + Python + AI)", y)
    for p in PROJECTS:
        y = ensure_space(c, y, needed_lines=3)
        y = draw_lines(c, wrap_text(f"• {p}", FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)
    y -= 6

    # Certs/Edu
    y = draw_section_header(c, "Certifications & Education", y)
    for ce in CERTS_EDU:
        y = ensure_space(c, y, needed_lines=2)
        y = draw_lines(c, wrap_text(f"• {ce}", FONT, FONT_SIZE, MAX_WIDTH), MARGIN_L, y)

    # Footer
    c.setFont(FONT, 8)
    c.drawRightString(PAGE_W - MARGIN_R, MARGIN_B - 10, f"Last updated: {date.today().isoformat()}")
    c.save()

if __name__ == "__main__":
    build_pdf(OUTPUT_PDF)
    print(f"Generated: {OUTPUT_PDF}")
