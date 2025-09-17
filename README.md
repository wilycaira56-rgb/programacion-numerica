# programacion-numerica
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Carátula - Universidad Nacional del Altiplano</title>
  <style>
    :root{--accent:#0b5ed7;--muted:#6b7280;--paper:#ffffff}
    html,body{height:100%;margin:0;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:#f3f4f6}
    .page{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px}
    .card{width:900px;max-width:100%;background:var(--paper);padding:48px;border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,0.08);text-align:center}
    .logo{height:90px;width:90px;border-radius:8px;background:linear-gradient(135deg,var(--accent),#06b6d4);display:inline-flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:20px;margin-bottom:18px}
    h1{font-size:20px;margin:6px 0;color:#111827}
    h2{font-size:16px;margin:4px 0;color:var(--muted);font-weight:600}
    .big-title{font-size:28px;font-weight:700;margin:18px 0 8px}
    .info{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:12px;align-items:start}
    .info .left{grid-column:1/3}
    .label{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:0.08em}
    .value{font-size:15px;font-weight:600;color:#0f172a}
    .footer{margin-top:28px;color:var(--muted);font-size:14px}
    @media (max-width:640px){.info{grid-template-columns:1fr}.logo{height:72px;width:72px}}
    /* estilos de impresión */
    @media print{
      body{background:white}
      .page{padding:0}
      .card{box-shadow:none;border-radius:0;padding:32mm}
    }
  </style>
</head>
<body>
  <div class="page">
    <div class="card">
      <div class="logo">UNA</div>
      <h1>Universidad Nacional del Altiplano - Puno</h1>
      <h2>Facultad de Ingeniería Estadística e Informática</h2>

      <div class="big-title">Carátula del trabajo</div>

      <div class="info">
        <div class="left">
          <div class="label">Curso</div>
          <div class="value">Programación Numérica</div>
        </div>

        <div>
          <div class="label">Docente</div>
          <div class="value">Fred Torres Cruz</div>
        </div>

        <div>
          <div class="label">Estudiante</div>
          <div class="value">Wily Calib Caira Huancollo</div>
        </div>

        <div>
          <div class="label">Departamento / Ciudad</div>
          <div class="value">Puno - Perú</div>
        </div>

        <div>
          <div class="label">Año</div>
          <div class="value">2025</div>
        </div>

        <div>
          <div class="label">Repositorio</div>
          <div class="value">(Pega el link de tu GitHub aquí)</div>
        </div>
      </div>

      <div class="footer">Diseñado para presentar trabajos del curso. Puedes editar el texto o descargar como PDF desde el navegador (Archivo → Imprimir → Guardar como PDF).</div>
    </div>
  </div>
</body>
</html>
