"""Work breakdown structure and register content.

Every field is either (a) traceable to the RC Vehicle Survey Report dated 30-Jun-2026,
or (b) a clearly-labelled proposed planning value / TBC placeholder. No dates, names,
equipment types or completion claims are invented.
"""

PM = "Kharsan Mujeb Al Ajmi"
TBC = "TBC"
DASH = "—"

CONFIRMED = "CONFIRMED (SURVEY): "

# Phase label -> Gantt colour group
PHASES = {
    "P1": ("Phase 1 — Project Preparation", "Preparation"),
    "P2": ("Phase 2 — Civil / Site Readiness", "Site Readiness"),
    "P3": ("Phase 3 — Engineering & Material Readiness", "Engineering"),
    "P4": ("Phase 4 — Installation", "Installation"),
    "P5": ("Phase 5 — Testing & Commissioning", "Testing"),
    "P6": ("Phase 6 — Handover", "Handover"),
}

# Fields:
#  id, phase_key, activity, location, predecessor, status, pct, responsible, role,
#  contractor, dependency, risk, approval, remarks, wk_start, wk_end, flag
# flag: "" | "CRITICAL" | "T2 POWER"
ACTIVITIES = [
    # ---------------- PHASE 1 — PROJECT PREPARATION ----------------
    ("1.01", "P1", "Project kickoff meeting and baseline agreement", "All trailers", DASH,
     "Not Started", 0, PM, "Project Manager", TBC,
     "Stakeholder availability", DASH, "No",
     "Kickoff to confirm scope, team, baseline dates and reporting cycle.", 1, 1, ""),

    ("1.02", "P1", "Site survey execution — RC Vehicle Survey", "Mobile / Trailer-based DC", DASH,
     "Completed", 1.0, TBC, "Survey Team", TBC,
     DASH, DASH, "No",
     CONFIRMED + "Survey carried out and reported on 30-Jun-2026. Completed prior to this baseline.",
     0, 0, ""),

    ("1.03", "P1", "Review of RC Vehicle Survey Report dated 30-Jun-2026", "All trailers", "1.02",
     "Ready to Start", 0, PM, "Project Manager", TBC,
     "Survey report issued (1.02 complete)", DASH, "No",
     "Source document is available; formal team review not yet recorded.", 1, 1, ""),

    ("1.04", "P1", "Scope confirmation — Fire Alarm System and Fire Suppression System", "All trailers", "1.03",
     "Not Started", 0, PM, "Project Manager", TBC,
     "Survey report review complete", DASH, "Yes",
     CONFIRMED + "Survey recommends providing a Fire Alarm System and a Fire Suppression System.",
     1, 2, ""),

    ("1.05", "P1", "Confirmation of project stakeholders, owner and governance", "N/A", "1.01",
     "Not Started", 0, PM, "Project Manager", TBC,
     "Project Owner nomination", "Project Owner not yet identified", "Yes",
     "Project Owner, Main Contractor, Fire System Contractor and Client Rep to be named.", 1, 2, ""),

    ("1.06", "P1", "Site readiness verification walkdown", "All trailers", "1.04",
     "Not Started", 0, TBC, "Site Supervisor", TBC,
     "Scope confirmed", "Site not yet ready — see Phase 2", "No",
     "Joint walkdown to baseline actual readiness against survey findings.", 2, 2, ""),

    ("1.07", "P1", "Confirmation of trailer availability", "All trailers", "1.06",
     "Not Started", 0, PM, "Project Manager", TBC,
     "Walkdown complete", DASH, "No",
     "Number and identity of trailers released for installation to be confirmed.", 2, 2, ""),

    ("1.08", "P1", "Confirmation of installation areas within trailers", "All trailers", "1.07",
     "Not Started", 0, TBC, "Fire & Life Safety Engineer", TBC,
     "Trailer availability confirmed", DASH, "No",
     "Installation areas to be agreed once partitions and rack layout are fixed.", 2, 2, ""),

    # ---------------- PHASE 2 — CIVIL / SITE READINESS ----------------
    ("2.01", "P2", "Completion of partition works", "Trailer-2", DASH,
     "In Progress", 0, TBC, "Civil / Partition Contractor", TBC,
     "Civil works front", "Ongoing partition works block power availability", "No",
     CONFIRMED + "Partition works are still ongoing in Trailer-2. Completion date and % progress TBC.",
     1, 4, "CRITICAL"),

    ("2.02", "P2", "Power source availability verification and energisation", "Trailer-2", "2.01",
     "Blocked", 0, TBC, "Electrical Contractor", TBC,
     "Completion of partition works + Power availability confirmation",
     "Trailer-2 power source currently unavailable", "Yes",
     CONFIRMED + "Power source in Trailer-2 is currently unavailable because partition works are ongoing.",
     4, 5, "T2 POWER"),

    ("2.03", "P2", "Verification of available installation areas", "All trailers", "1.08",
     "Not Started", 0, TBC, "Site Supervisor", TBC,
     "Installation areas confirmed", DASH, "No",
     "Physical verification of clear areas for alarm and suppression equipment.", 2, 3, ""),

    ("2.04", "P2", "Installation of Racks and Cabinets", "All trailers", "2.03",
     "Not Started", 0, TBC, "Main Contractor", TBC,
     "Installation areas verified", "Racks and Cabinets installation not yet started", "No",
     CONFIRMED + "Installation of Racks and Cabinets has not yet started in the available trailers.",
     3, 6, "CRITICAL"),

    ("2.05", "P2", "Racks and Cabinets readiness confirmation / sign-off", "All trailers", "2.04",
     "Not Started", 0, TBC, "QA/QC", TBC,
     "Racks and Cabinets installation complete", "Racks and Cabinets not yet started", "Yes",
     "Gate for all rack/cabinet-interfacing fire system activities.", 6, 6, "CRITICAL"),

    ("2.06", "P2", "Power availability verification — trailers other than Trailer-2", "All trailers", "1.07",
     "Not Started", 0, TBC, "Electrical Contractor", TBC,
     "Trailer availability confirmed",
     "Survey confirms unavailability for Trailer-2 only; other trailers to be verified", "No",
     "Source confirms the power constraint for Trailer-2. Status of remaining trailers TBC.", 2, 3, ""),

    ("2.07", "P2", "Access, HSE induction and work permit readiness", "All trailers", "1.01",
     "Not Started", 0, TBC, "HSE", TBC,
     "Kickoff complete", DASH, "Yes",
     "Permit-to-work regime, hot work and access control to be established.", 2, 3, ""),

    # ---------------- PHASE 3 — ENGINEERING & MATERIAL READINESS ----------------
    ("3.01", "P3", "Fire suppression system design review", "All trailers", "1.04",
     "Not Started", 0, TBC, "Fire Suppression Engineer", TBC,
     "Scope confirmed", DASH, "No",
     "Design basis, agent type and coverage to be confirmed during engineering/design.", 2, 3, ""),

    ("3.02", "P3", "Fire alarm system design review", "All trailers", "1.04",
     "Not Started", 0, TBC, "Fire Alarm Engineer", TBC,
     "Scope confirmed", DASH, "No",
     "Detection philosophy and panel architecture to be confirmed during engineering/design.", 2, 3, ""),

    ("3.03", "P3", "Equipment and material confirmation", "All trailers", "3.01",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "Design reviews complete", DASH, "No",
     "Equipment types not specified in the survey — to be confirmed during engineering/design.", 3, 4, ""),

    ("3.04", "P3", "Shop drawing and technical submittal preparation", "All trailers", "3.03",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "Material list confirmed", DASH, "No",
     "Submittal package covering both recommended systems.", 3, 4, ""),

    ("3.05", "P3", "Shop drawing and material approval", "All trailers", "3.04",
     "Pending Approval", 0, TBC, "Client Representative", TBC,
     "Submittal issued", "Approval turnaround not yet agreed", "Yes",
     "Approving authority and review duration to be confirmed.", 5, 5, "CRITICAL"),

    ("3.06", "P3", "Procurement and purchase order release", "All trailers", "3.05",
     "Pending Material", 0, TBC, "Main Contractor", TBC,
     "Material approval obtained", "Long-lead items may drive the critical path", "Yes",
     "Lead times unknown until equipment selection is confirmed.", 5, 6, "CRITICAL"),

    ("3.07", "P3", "Manufacturing, delivery to site and material inspection", "All trailers", "3.06",
     "Pending Material", 0, TBC, "Main Contractor", TBC,
     "Purchase orders placed", "Delivery lead time TBC", "No",
     "Material availability is a gate for the start of Phase 4.", 6, 8, "CRITICAL"),

    # ---------------- PHASE 4 — INSTALLATION ----------------
    ("4.01", "P4", "Fire alarm system installation — containment and cabling", "All trailers", "3.07",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "Material on site + Racks and Cabinets ready (2.05)",
     "Racks and Cabinets installation not yet started", "No",
     "First installation front; cannot start before site readiness gates are closed.", 8, 9, "CRITICAL"),

    ("4.02", "P4", "Fire detection devices installation", "All trailers", "4.01",
     "Not Started", 0, TBC, "Fire Alarm Engineer", TBC,
     "Containment and cabling complete", DASH, "No",
     "Device types to be confirmed during engineering/design.", 9, 10, ""),

    ("4.03", "P4", "Fire alarm control and monitoring equipment installation", "All trailers", "4.01",
     "Not Started", 0, TBC, "Fire Alarm Engineer", TBC,
     "Containment and cabling complete", DASH, "No",
     "Control/monitoring equipment scope to be confirmed during engineering/design.", 9, 10, ""),

    ("4.04", "P4", "Fire suppression system installation — mounting and supports", "All trailers", "3.07",
     "Not Started", 0, TBC, "Fire Suppression Engineer", TBC,
     "Material on site + Racks and Cabinets ready (2.05)",
     "Racks and Cabinets installation not yet started", "No",
     "Suppression system recommended by the survey; configuration TBC in design.", 8, 10, "CRITICAL"),

    ("4.05", "P4", "Suppression equipment installation", "All trailers", "4.04",
     "Not Started", 0, TBC, "Fire Suppression Engineer", TBC,
     "Mounting and supports complete", DASH, "No",
     "Equipment types to be confirmed during engineering/design.", 10, 11, ""),

    ("4.06", "P4", "Piping / tubing and associated components installation (where applicable)",
     "All trailers", "4.05",
     "Not Started", 0, TBC, "Fire Suppression Engineer", TBC,
     "Suppression equipment installed", DASH, "No",
     "Applicability depends on the suppression solution confirmed during design.", 10, 11, ""),

    ("4.07", "P4", "Interfaces with racks and cabinets", "All trailers", "2.05",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "Racks and Cabinets ready (2.05)",
     "Racks and Cabinets installation not yet started", "No",
     "Directly gated by the rack/cabinet readiness constraint recorded in the survey.", 11, 11, "CRITICAL"),

    ("4.08", "P4", "Power and control connections", "Trailer-2 / All trailers", "2.02",
     "Blocked", 0, TBC, "Electrical Contractor", TBC,
     "Completion of partition works + Power availability confirmation (Trailer-2)",
     "Trailer-2 power source currently unavailable", "No",
     CONFIRMED + "Cannot proceed in Trailer-2 until partition works finish and power is available.",
     11, 12, "T2 POWER"),

    ("4.09", "P4", "System integration — fire alarm and fire suppression", "All trailers", "4.08",
     "Not Started", 0, TBC, "Fire & Life Safety Engineer", TBC,
     "Power and control connections complete",
     "Dependent on Trailer-2 power availability", "No",
     "Integration scope with DC systems to be confirmed during design.", 12, 12, "CRITICAL"),

    # ---------------- PHASE 5 — TESTING & COMMISSIONING ----------------
    ("5.01", "P5", "Installation inspection", "All trailers", "4.09",
     "Not Started", 0, TBC, "QA/QC", TBC,
     "Installation complete", DASH, "Yes",
     "Inspection and test plan to be issued during engineering.", 12, 12, ""),

    ("5.02", "P5", "Cable and connection verification", "All trailers", "5.01",
     "Not Started", 0, TBC, "Testing & Commissioning Lead", TBC,
     "Installation inspection passed", DASH, "No",
     "Continuity, insulation and termination checks.", 12, 12, ""),

    ("5.03", "P5", "Fire alarm system testing", "All trailers", "5.02",
     "Not Started", 0, TBC, "Fire Alarm Engineer", TBC,
     "Cable and connection verification complete", DASH, "No",
     "Test procedure to be approved before execution.", 13, 13, ""),

    ("5.04", "P5", "Fire suppression system testing", "All trailers", "5.02",
     "Not Started", 0, TBC, "Fire Suppression Engineer", TBC,
     "Cable and connection verification complete", DASH, "No",
     "Test procedure to be approved before execution.", 13, 13, ""),

    ("5.05", "P5", "Functional testing", "All trailers", "5.03",
     "Not Started", 0, TBC, "Testing & Commissioning Lead", TBC,
     "System testing complete", "Requires stable power supply in all trailers", "No",
     "Cause-and-effect matrix to be produced during engineering.", 14, 14, "CRITICAL"),

    ("5.06", "P5", "Integration testing", "All trailers", "5.05",
     "Not Started", 0, TBC, "Fire & Life Safety Engineer", TBC,
     "Functional testing complete", DASH, "No",
     "End-to-end verification across both recommended systems.", 14, 14, ""),

    ("5.07", "P5", "Defect identification and punch list issue", "All trailers", "5.06",
     "Not Started", 0, TBC, "QA/QC", TBC,
     "Integration testing complete", DASH, "No",
     "Punch list to be logged in the Action Tracker.", 15, 15, ""),

    ("5.08", "P5", "Rectification of defects", "All trailers", "5.07",
     "Not Started", 0, TBC, "Main Contractor", TBC,
     "Punch list issued", DASH, "No",
     "Rectification duration depends on defect volume — TBC.", 15, 15, ""),

    ("5.09", "P5", "Retesting and verification", "All trailers", "5.08",
     "Not Started", 0, TBC, "Testing & Commissioning Lead", TBC,
     "Defects rectified", DASH, "Yes",
     "Retest scope limited to rectified items plus affected functions.", 16, 16, ""),

    # ---------------- PHASE 6 — HANDOVER ----------------
    ("6.01", "P6", "Final inspection", "All trailers", "5.09",
     "Not Started", 0, TBC, "QA/QC", TBC,
     "Retesting complete", DASH, "Yes",
     "Joint inspection with Client Representative.", 16, 16, ""),

    ("6.02", "P6", "Punch list closure", "All trailers", "6.01",
     "Not Started", 0, TBC, "Main Contractor", TBC,
     "Final inspection complete", DASH, "No",
     "Zero open critical items required for acceptance.", 16, 16, ""),

    ("6.03", "P6", "As-built documentation", "All trailers", "6.02",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "Punch list closed", DASH, "No",
     "As-builts to reflect final installed configuration.", 16, 17, ""),

    ("6.04", "P6", "Test reports compilation and submission", "All trailers", "5.09",
     "Not Started", 0, TBC, "Testing & Commissioning Lead", TBC,
     "Retesting complete", DASH, "Yes",
     "Signed test records for both recommended systems.", 17, 17, ""),

    ("6.05", "P6", "Operation and Maintenance (O&M) documentation", "All trailers", "6.03",
     "Not Started", 0, TBC, "Fire System Specialist", TBC,
     "As-builts issued", DASH, "Yes",
     "O&M manuals and spare parts list.", 17, 17, ""),

    ("6.06", "P6", "Operator and end-user training", "All trailers", "6.05",
     "Not Started", 0, TBC, "Fire & Life Safety Engineer", TBC,
     "O&M documentation issued", DASH, "No",
     "Trainee list and duration to be confirmed by the Project Owner.", 17, 17, ""),

    ("6.07", "P6", "Final acceptance and client sign-off", "All trailers", "6.06",
     "Not Started", 0, TBC, "Client Representative", TBC,
     "Training complete + documentation accepted", DASH, "Yes",
     "Acceptance criteria to be agreed at kickoff.", 18, 18, "CRITICAL"),

    ("6.08", "P6", "System handover to operations", "All trailers", "6.07",
     "Not Started", 0, TBC, "Project Owner", TBC,
     "Final acceptance obtained", DASH, "Yes",
     "Handover certificate and key/asset transfer.", 18, 18, "CRITICAL"),

    ("6.09", "P6", "Project closeout", "All trailers", "6.08",
     "Not Started", 0, PM, "Project Manager", TBC,
     "Handover complete", DASH, "Yes",
     "Final account, lessons learned and document archive.", 18, 18, ""),
]

# ---------------------------------------------------------------------------
# MILESTONES (brief section 9)
# ---------------------------------------------------------------------------
MILESTONES = [
    ("M01", "Project Kickoff",            "TBD", TBC, "Not Started",      "Stakeholder confirmation",                          "Baseline agreement and governance sign-off."),
    ("M02", "Site Readiness Confirmed",   "TBD", TBC, "Not Started",      "Partition works + installation area verification",  "Gate for all site activities."),
    ("M03", "Power Available (Trailer-2)","TBD", TBC, "Blocked",          "Completion of partition works",                     "CONFIRMED constraint: Trailer-2 power source currently unavailable."),
    ("M04", "Racks & Cabinets Ready",     "TBD", TBC, "Not Started",      "Installation of Racks and Cabinets (2.04)",          "CONFIRMED constraint: installation has not yet started."),
    ("M05", "Engineering Approved",       "TBD", TBC, "Pending Approval", "Shop drawing and material approval (3.05)",          "Approving authority to be confirmed."),
    ("M06", "Materials Available on Site","TBD", TBC, "Pending Material", "Procurement and delivery (3.06 / 3.07)",             "Lead times unknown until equipment selection is confirmed."),
    ("M07", "Installation Start",         "TBD", TBC, "Not Started",      "M02 + M04 + M06",                                    "Cannot start before all three readiness gates close."),
    ("M08", "Installation Complete",      "TBD", TBC, "Not Started",      "System integration (4.09)",                          "Includes power and control connections."),
    ("M09", "Testing Complete",           "TBD", TBC, "Not Started",      "Integration testing (5.06)",                         "Both recommended systems tested."),
    ("M10", "Defects Closed",             "TBD", TBC, "Not Started",      "Rectification and retesting (5.08 / 5.09)",          "Zero open critical defects."),
    ("M11", "Final Acceptance",           "TBD", TBC, "Not Started",      "Final acceptance and sign-off (6.07)",               "Acceptance criteria to be agreed at kickoff."),
    ("M12", "Handover",                   "TBD", TBC, "Not Started",      "System handover to operations (6.08)",               "Handover certificate issued."),
    ("M13", "Project Closeout",           "TBD", TBC, "Not Started",      "Project closeout (6.09)",                            "Overall project completion date TBD."),
]

# ---------------------------------------------------------------------------
# RESPONSIBILITY MATRIX (brief section 6)
# ---------------------------------------------------------------------------
RESPONSIBILITY = [
    ("Project Ownership",        TBC, "Project Owner",                 TBC, "Overall accountability, funding, acceptance and handover authority.", TBC, "Not Started"),
    ("Project Management",       PM,  "Project Manager",               TBC, "Day-to-day management, schedule, reporting and stakeholder coordination.", TBC, "In Progress"),
    ("Fire & Life Safety",       TBC, "Fire & Life Safety Engineer",   TBC, "Design compliance, integration and life-safety assurance.", TBC, "Not Started"),
    ("Fire Alarm Engineering",   TBC, "Fire Alarm Engineer",           TBC, "Fire alarm design review, installation supervision and testing.", TBC, "Not Started"),
    ("Fire Suppression Engineering", TBC, "Fire Suppression Engineer", TBC, "Fire suppression design review, installation supervision and testing.", TBC, "Not Started"),
    ("Site Supervision",         TBC, "Site Supervisor",               TBC, "Daily site control, work fronts, coordination between trades.", TBC, "Not Started"),
    ("Main Works",               TBC, "Main Contractor",               TBC, "Overall construction delivery including racks and cabinets installation.", TBC, "Not Started"),
    ("Fire System Delivery",     TBC, "Fire System Specialist",        TBC, "Supply and installation of the recommended fire alarm and suppression systems.", TBC, "Not Started"),
    ("Electrical Works",         TBC, "Electrical Contractor",         TBC, "Power supply, energisation and power/control connections.", TBC, "Not Started"),
    ("Civil / Partition Works",  TBC, "Civil / Partition Contractor",  TBC, "Partition works in Trailer-2 — currently ongoing per survey.", TBC, "In Progress"),
    ("Quality Assurance",        TBC, "QA/QC",                         TBC, "Inspection, ITP execution, punch list management and sign-off.", TBC, "Not Started"),
    ("Health, Safety & Environment", TBC, "HSE",                       TBC, "Permits, inductions, risk assessments and site safety compliance.", TBC, "Not Started"),
    ("Testing & Commissioning",  TBC, "Testing & Commissioning Lead",  TBC, "Test procedures, functional and integration testing, test records.", TBC, "Not Started"),
    ("Client Interface",         TBC, "Client Representative",         TBC, "Approvals, witnessing, final acceptance and handover receipt.", TBC, "Not Started"),
]

# ---------------------------------------------------------------------------
# ACTION TRACKER (brief section 13)
# ---------------------------------------------------------------------------
ACTIONS = [
    ("A01", "Complete partition works in Trailer-2",
     "Survey confirms partition works are still ongoing, which is blocking the power source.",
     "Civil / Partition Contractor (TBC)", "TBD", "Critical", "In Progress", "Yes",
     "CRITICAL PATH — first link in the Trailer-2 readiness chain."),
    ("A02", "Confirm power availability in Trailer-2 once partitions are complete",
     "Survey confirms the Trailer-2 power source is currently unavailable.",
     "Electrical Contractor (TBC)", "TBD", "Critical", "Blocked", "Yes",
     "CRITICAL PATH — gates power and control connections and functional testing."),
    ("A03", "Start and complete installation of Racks and Cabinets",
     "Survey confirms rack and cabinet installation has not yet started in the available trailers.",
     "Main Contractor (TBC)", "TBD", "Critical", "Not Started", "Yes",
     "CRITICAL PATH — gates all rack/cabinet-interfacing fire system works."),
    ("A04", "Confirm overall site readiness and release installation work fronts",
     "Installation cannot be released until partitions, power and racks/cabinets are confirmed ready.",
     "Project Manager — " + PM, "TBD", "Critical", "Not Started", "Yes",
     "Sequence: A01 → A02 → A03 → A04 → release Phase 4."),
    ("A05", "Nominate the Project Owner and confirm the governance structure",
     "No project owner is identified in the source document; approvals cannot be routed.",
     "Project Manager — " + PM, "TBD", "High", "Not Started", "Yes",
     "Required before any approval-gated activity can complete."),
    ("A06", "Appoint the Main Contractor and Fire System Contractor",
     "No contractor is named in the source document.",
     "Project Owner (TBC)", "TBD", "High", "Not Started", "Yes",
     "Required to resource Phases 2 to 6."),
    ("A07", "Confirm fire alarm and fire suppression design basis and equipment selection",
     "The survey recommends both systems but does not specify equipment types.",
     "Fire & Life Safety Engineer (TBC)", "TBD", "High", "Not Started", "No",
     "Equipment types to be confirmed during engineering/design."),
    ("A08", "Establish and approve the project baseline dates",
     "The source document provides no start, duration or completion dates.",
     "Project Manager — " + PM, "TBD", "High", "Not Started", "No",
     "Converts the proposed relative baseline into confirmed calendar dates."),
    ("A09", "Confirm procurement lead times for the approved materials",
     "Long-lead items may govern the installation start date.",
     "Main Contractor (TBC)", "TBD", "Medium", "Not Started", "No",
     "Feeds milestone M06 — Materials Available on Site."),
    ("A10", "Confirm the power availability status of all trailers other than Trailer-2",
     "The survey confirms the constraint for Trailer-2 only; other trailers are not addressed.",
     "Electrical Contractor (TBC)", "TBD", "Medium", "Not Started", "No",
     "Closes an open information gap in the source document."),
    ("A11", "Establish the permit-to-work and HSE regime for trailer works",
     "Work cannot commence without access and permit readiness.",
     "HSE (TBC)", "TBD", "Medium", "Not Started", "No",
     "Prerequisite for all site work fronts."),
    ("A12", "Agree the approval authority and review turnaround for submittals",
     "Approval route is undefined, which puts the engineering gate at risk.",
     "Client Representative (TBC)", "TBD", "Medium", "Not Started", "No",
     "Feeds milestone M05 — Engineering Approved."),
]

# ---------------------------------------------------------------------------
# RISK REGISTER (brief section 14)
# ---------------------------------------------------------------------------
CONF_RISK = "Source-confirmed constraint"
PLAN_RISK = "Planning Risk — To Be Validated"

RISKS = [
    ("R01", "Trailer-2 power source remains unavailable",
     "Partition works in Trailer-2 are still ongoing (confirmed by survey).",
     "Power and control connections, functional testing and Trailer-2 handover cannot proceed.",
     "High", "High",
     "Expedite partition works; agree a firm completion date; confirm energisation plan; consider a temporary certified supply if approved.",
     "Civil / Partition Contractor (TBC)", "TBD", "Open", CONF_RISK),
    ("R02", "Racks and Cabinets installation has not started",
     "Rack and cabinet works not yet commenced in the available trailers (confirmed by survey).",
     "All rack/cabinet-interfacing fire alarm and suppression activities are gated; installation start slips.",
     "High", "High",
     "Confirm rack/cabinet scope, contractor and start date; sequence rack installation ahead of fire system works.",
     "Main Contractor (TBC)", "TBD", "Open", CONF_RISK),
    ("R03", "No confirmed project baseline dates",
     "The source document provides no start, duration or completion dates.",
     "Progress cannot be measured; delay cannot be evidenced; no contractual float visibility.",
     "High", "Medium",
     "Convert the proposed relative baseline into calendar dates at kickoff and freeze as Version 1.0.",
     "Project Manager — " + PM, "TBD", "Open", PLAN_RISK),
    ("R04", "Project Owner and contractors not yet appointed",
     "No owner or contractor is identified in the source document.",
     "Approvals stall; no accountable party for the critical path actions.",
     "High", "Medium",
     "Nominate the Project Owner and award the main and fire system packages before Phase 3 approvals.",
     "Project Owner (TBC)", "TBD", "Open", PLAN_RISK),
    ("R05", "Equipment selection not yet defined",
     "The survey recommends the systems but does not specify equipment types.",
     "Procurement cannot start; lead times remain unknown; installation start date unreliable.",
     "Medium", "High",
     "Complete design reviews and freeze the material schedule before releasing purchase orders.",
     "Fire & Life Safety Engineer (TBC)", "TBD", "Open", PLAN_RISK),
    ("R06", "Long procurement lead times govern the critical path",
     "Fire suppression equipment can carry extended manufacturing lead times.",
     "Installation start is deferred; overall completion date slips.",
     "Medium", "High",
     "Obtain lead-time confirmation at quotation stage; pre-order long-lead items after approval.",
     "Main Contractor (TBC)", "TBD", "Open", PLAN_RISK),
    ("R07", "Approval turnaround for submittals is undefined",
     "No approval authority or review duration has been agreed.",
     "Engineering gate slips and delays procurement release.",
     "Medium", "Medium",
     "Agree the approval matrix and a maximum review turnaround at kickoff.",
     "Client Representative (TBC)", "TBD", "Open", PLAN_RISK),
    ("R08", "Trade congestion inside the trailers",
     "Civil, electrical, rack and fire system trades share a confined trailer envelope.",
     "Work front conflicts, rework and reduced productivity.",
     "Medium", "Medium",
     "Produce a sequenced work-front plan and a shared trailer access schedule.",
     "Site Supervisor (TBC)", "TBD", "Open", PLAN_RISK),
    ("R09", "Power availability of remaining trailers unverified",
     "The survey addresses the Trailer-2 power constraint only.",
     "A further power constraint may emerge late and block additional work fronts.",
     "Medium", "Medium",
     "Verify and record the power status of every trailer before releasing installation.",
     "Electrical Contractor (TBC)", "TBD", "Open", PLAN_RISK),
    ("R10", "Interface between fire systems and DC racks not yet defined",
     "Rack layout and installation areas are not yet fixed.",
     "Detection coverage and suppression arrangement may require redesign after rack installation.",
     "Medium", "Medium",
     "Freeze the rack layout before finalising detection and suppression shop drawings.",
     "Fire & Life Safety Engineer (TBC)", "TBD", "Open", PLAN_RISK),
]

# ---------------------------------------------------------------------------
# CRITICAL DEPENDENCIES (brief section 8)
# ---------------------------------------------------------------------------
DEPENDENCIES = [
    ("CD-01", "Trailer-2 power source is currently unavailable.",
     "Partition works are still ongoing.",
     "Completion of partition works + power availability confirmation.",
     "Complete partition works in Trailer-2, then verify and energise the power source.",
     "Civil / Partition Contractor (TBC) → Electrical Contractor (TBC)",
     "TBD",
     "Blocks activity 2.02 and 4.08, and gates functional testing (5.05) and Trailer-2 handover.",
     "CONFIRMED CONSTRAINT (SURVEY)"),
    ("CD-02", "Installation of Racks and Cabinets has not yet started in the available trailers.",
     "Rack and cabinet works not yet commenced.",
     "Completion and readiness sign-off of racks and cabinets (2.04 → 2.05).",
     "Confirm scope, contractor and start date for racks and cabinets installation.",
     "Main Contractor (TBC)",
     "TBD",
     "Gates activities 4.01, 4.04 and 4.07, and therefore the entire installation phase.",
     "CONFIRMED CONSTRAINT (SURVEY)"),
]
