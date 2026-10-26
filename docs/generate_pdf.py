import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf():
    pdf_path = r"F:\Users\Max\Desktop\moviles\taller 4\docs\entregable_taller.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#1E3A8A")
    secondary_color = colors.HexColor("#F59E0B")
    dark_text = colors.HexColor("#0F172A")
    muted_text = colors.HexColor("#475569")
    bg_light = colors.HexColor("#F8FAFC")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#B45309"),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=dark_text
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=dark_text
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1E293B")
    )

    story = []

    # Title & Badge
    story.append(Paragraph("TALLER PRÁCTICO — DESARROLLO DE APLICACIONES MÓVILES", subtitle_style))
    story.append(Paragraph("🇨🇴 Datos Abiertos de Colombia (Flutter)", title_style))
    story.append(HRFlowable(width="100%", thickness=2.5, color=primary_color, spaceBefore=4, spaceAfter=10))

    # Metadata Box
    meta_data = [
        [Paragraph("<b>Autor:</b>", body_style), Paragraph("Samuel Rincón (UCEVA)", body_style)],
        [Paragraph("<b>Repositorio Público:</b>", body_style), Paragraph('<font color="#1E3A8A"><u>https://github.com/Sarincon508/taller_datos_abiertos</u></font>', body_style)],
        [Paragraph("<b>Ramas GitFlow:</b>", body_style), Paragraph("<b>main</b> (producción) • <b>dev</b> (integración) • <b>feature/taller_api_colombia</b>", body_style)],
        [Paragraph("<b>API Oficial:</b>", body_style), Paragraph("API Colombia v1 (https://api-colombia.com/)", body_style)],
        [Paragraph("<b>Paquetes Clave:</b>", body_style), Paragraph("<b>http</b> (^1.6.0) • <b>go_router</b> (^18.1.1) • <b>flutter_dotenv</b> (^6.0.1) • <b>intl</b> (^0.20.3)", body_style)],
    ]

    meta_table = Table(meta_data, colWidths=[130, 410])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_light),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Endpoints
    story.append(Paragraph("1. Endpoints de API Colombia Seleccionados (Mínimo 4)", h1_style))
    story.append(Paragraph("Se implementó consumo completo en dos niveles (Listado general y Detalle por ID) con decodificación UTF-8 para garantizar soporte de caracteres especiales y acentos:", body_style))
    story.append(Spacer(1, 4))

    endpoints_data = [
        [
            Paragraph("Módulo / Recurso", table_header_style),
            Paragraph("Ruta Listado (GET)", table_header_style),
            Paragraph("Ruta Detalle (GET)", table_header_style),
            Paragraph("Información Extraída y Atributos", table_header_style)
        ],
        [
            Paragraph("<b>1. Departamentos</b>", table_cell_style),
            Paragraph("/api/v1/Department", code_style),
            Paragraph("/api/v1/Department/{id}", code_style),
            Paragraph("32 departamentos, capital, población, superficie (km²), municipios y prefijo telefónico.", table_cell_style)
        ],
        [
            Paragraph("<b>2. Atracciones Turísticas</b>", table_cell_style),
            Paragraph("/api/v1/TouristicAttraction", code_style),
            Paragraph("/api/v1/TouristicAttraction/{id}", code_style),
            Paragraph("Parques naturales, monumentos, coordenadas lat/lon, galería fotográfica y ciudad.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Presidentes</b>", table_cell_style),
            Paragraph("/api/v1/President", code_style),
            Paragraph("/api/v1/President/{id}", code_style),
            Paragraph("Mandatarios de la República, periodos, partido político, retrato oficial y biografía.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Platos Típicos</b>", table_cell_style),
            Paragraph("/api/v1/TypicalDish", code_style),
            Paragraph("/api/v1/TypicalDish/{id}", code_style),
            Paragraph("Gastronomía regional, fotografía, desglose de ingredientes y departamento de origen.", table_cell_style)
        ],
    ]

    endpoints_table = Table(endpoints_data, colWidths=[110, 125, 135, 170])
    endpoints_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(endpoints_table)
    story.append(Spacer(1, 10))

    # 2. Arquitectura
    story.append(Paragraph("2. Arquitectura y Estructura por Capas", h1_style))
    story.append(Paragraph("La aplicación adopta una arquitectura modular limpia con separación estricta de responsabilidades:", body_style))
    story.append(Spacer(1, 4))

    arch_data = [
        [Paragraph("<b>Capa</b>", table_header_style), Paragraph("Ubicación", table_header_style), Paragraph("Responsabilidad Técnica", table_header_style)],
        [Paragraph("<b>Config</b>", table_cell_style), Paragraph("lib/config/", code_style), Paragraph("Carga de variables de entorno (.env) mediante <code>Environment</code> con fallbacks y constantes.", table_cell_style)],
        [Paragraph("<b>Models</b>", table_cell_style), Paragraph("lib/models/", code_style), Paragraph("Entidades fuertemente tipadas con serialización <code>fromJson</code> y <code>toJson</code> para cada endpoint.", table_cell_style)],
        [Paragraph("<b>Services</b>", table_cell_style), Paragraph("lib/services/", code_style), Paragraph("Cliente <code>ApiColombiaService</code> con manejo de <code>ApiException</code>, status codes (200, 404, 500) y timeouts.", table_cell_style)],
        [Paragraph("<b>Routes</b>", table_cell_style), Paragraph("lib/routes/", code_style), Paragraph("Configuración declarativa de <code>go_router</code> con subrutas, nombres de ruta y paso de parámetros.", table_cell_style)],
        [Paragraph("<b>Themes</b>", table_cell_style), Paragraph("lib/themes/", code_style), Paragraph("Temas Material 3 claro y oscuro con identidad tricolor colombiana (azul, oro, esmeralda, carmesí).", table_cell_style)],
        [Paragraph("<b>Views</b>", table_cell_style), Paragraph("lib/views/", code_style), Paragraph("Pantallas principales: Dashboard interactivo, 4 Listados con búsqueda en vivo y 4 Detalles completos.", table_cell_style)],
        [Paragraph("<b>Widgets</b>", table_cell_style), Paragraph("lib/widgets/", code_style), Paragraph("Componentes reutilizables: <code>LoadingView</code>, <code>ErrorView</code>, <code>EmptyView</code>, <code>CustomSearchBar</code>, etc.", table_cell_style)],
    ]

    arch_table = Table(arch_data, colWidths=[70, 110, 360])
    arch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(arch_table)
    story.append(Spacer(1, 10))

    # 3. Navegación go_router
    story.append(Paragraph("3. Navegación Maestro-Detalle con go_router", h1_style))
    story.append(Paragraph("Todas las rutas están declaradas con nombre y path jerárquico. El paso de parámetros soporta tanto <code>pathParameters</code> (ID de registro) como paso instantáneo mediante <code>extra</code>, permitiendo también deep-linking directo:", body_style))
    story.append(Spacer(1, 4))

    routes_data = [
        [Paragraph("Nombre de Ruta", table_header_style), Paragraph("Path", table_header_style), Paragraph("Parámetros", table_header_style), Paragraph("Pantalla Destino", table_header_style)],
        [Paragraph("dashboard", code_style), Paragraph("/", code_style), Paragraph("Ninguno", table_cell_style), Paragraph("DashboardView", table_cell_style)],
        [Paragraph("departments", code_style), Paragraph("/departments", code_style), Paragraph("Ninguno", table_cell_style), Paragraph("DepartmentsListView", table_cell_style)],
        [Paragraph("department-detail", code_style), Paragraph("/departments/:id", code_style), Paragraph(":id (int), extra: Department?", table_cell_style), Paragraph("DepartmentDetailView", table_cell_style)],
        [Paragraph("attractions", code_style), Paragraph("/attractions", code_style), Paragraph("Ninguno", table_cell_style), Paragraph("AttractionsListView", table_cell_style)],
        [Paragraph("attraction-detail", code_style), Paragraph("/attractions/:id", code_style), Paragraph(":id (int), extra: TouristicAttraction?", table_cell_style), Paragraph("AttractionDetailView", table_cell_style)],
        [Paragraph("presidents", code_style), Paragraph("/presidents", code_style), Paragraph("Ninguno", table_cell_style), Paragraph("PresidentsListView", table_cell_style)],
        [Paragraph("president-detail", code_style), Paragraph("/presidents/:id", code_style), Paragraph(":id (int), extra: President?", table_cell_style), Paragraph("PresidentDetailView", table_cell_style)],
        [Paragraph("typical-dishes", code_style), Paragraph("/typical-dishes", code_style), Paragraph("Ninguno", table_cell_style), Paragraph("TypicalDishesListView", table_cell_style)],
        [Paragraph("typical-dish-detail", code_style), Paragraph("/typical-dishes/:id", code_style), Paragraph(":id (int), extra: TypicalDish?", table_cell_style), Paragraph("TypicalDishDetailView", table_cell_style)],
    ]

    routes_table = Table(routes_data, colWidths=[110, 115, 160, 155])
    routes_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(routes_table)
    story.append(Spacer(1, 10))

    # 4. Manejo de Estados y GitFlow
    story.append(Paragraph("4. Manejo de Estados y Flujo GitFlow", h1_style))
    story.append(Paragraph("<b>Manejo de Estados:</b> Cada módulo implementa 4 estados visuales claros: (1) <b>Cargando</b> (spinner animado con mensaje contextual), (2) <b>Éxito</b> (ListView.builder con pull-to-refresh), (3) <b>Error</b> (código HTTP 404/500/red con botón Reintentar), y (4) <b>Búsqueda vacía</b>.<br/>"
                           "<b>Flujo GitFlow:</b> El repositorio cuenta con la estructura formal de ramas: <b>main</b> (versión estable), <b>dev</b> (integración) y <b>feature/taller_api_colombia</b>. Se realizaron 9 commits atómicos con la convención Conventional Commits (feat, test, docs) e integración mediante merge commits <code>--no-ff</code> que simulan el Pull Request.", body_style))

    doc.build(story)
    print("PDF generated successfully at:", pdf_path)

if __name__ == "__main__":
    generate_pdf()
