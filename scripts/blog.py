"""Blog posts (Spanish). scripts/build.py renders /blog/ and /blog/<slug>/.

Each post opens with a short direct answer (what search engines and AI assistants
quote), uses question-style headings, and lists its sources. Figures were checked
in Oct 2026; when they change (loan limits, CalHFA rounds, medians) update the post
and its 'updated' date.
"""

PUBLISHED = '2026-10-26'

POSTS = [
    {
        'slug': 'comprar-casa-con-itin-california',
        'category': 'Comprar',
        'title': 'Cómo comprar casa con ITIN en California (2026): requisitos, enganche y pasos',
        'seo_title': 'Comprar casa con ITIN en California (2026): requisitos y pasos',
        'desc': '¿Se puede comprar casa con ITIN en California? Sí. Requisitos, cuánto enganche piden (normalmente 15% a 20%), documentos y los pasos para comprar en el Bay Area.',
        'keywords': ['comprar casa con ITIN', 'préstamo ITIN California', 'hipoteca sin seguro social', 'comprar casa sin papeles California'],
        'cities': ['pittsburg', 'antioch', 'richmond'],
        'related': ['cuanto-enganche-para-comprar-casa-california', 'costos-de-cierre-comprador-california', 'programas-primera-casa-california'],
        'answer': 'Sí, puedes comprar casa en California con un ITIN en lugar de número de Seguro Social. Necesitas un préstamo hipotecario ITIN de un prestamista que lo ofrezca. En California normalmente piden entre 15% y 20% de enganche, dos años de declaraciones de impuestos con tu ITIN e historial de crédito, y la tasa suele ser más alta que la de un préstamo convencional.',
        'body': '''
<h2>¿Qué es un ITIN y por qué importa para comprar casa?</h2>
<p>El ITIN (Número de Identificación Personal del Contribuyente) lo emite el IRS para que personas sin número de Seguro Social puedan declarar impuestos. Es un número fiscal, no un documento migratorio, y es la base para que muchas familias construyan historial financiero en Estados Unidos.</p>
<p>Los préstamos más comunes, como FHA y los convencionales de Fannie Mae y Freddie Mac, piden número de Seguro Social válido y un estatus migratorio que califique. Por eso, quien solo tiene ITIN compra con un <strong>préstamo ITIN</strong>: un préstamo "non-QM" que algunos bancos y prestamistas ofrecen con sus propias reglas.</p>

<h2>¿Qué requisitos piden para un préstamo ITIN?</h2>
<p>Cada prestamista pone sus condiciones, pero estos son los requisitos más comunes en California:</p>
<table>
<thead><tr><th>Requisito</th><th>Lo más común</th></tr></thead>
<tbody>
<tr><td>Identificación</td><td>ITIN vigente y una identificación con foto (por ejemplo, pasaporte o matrícula consular)</td></tr>
<tr><td>Enganche</td><td>Entre 15% y 20% del precio en California; algunos prestamistas piden hasta 25%</td></tr>
<tr><td>Impuestos</td><td>Dos años de declaraciones presentadas con tu ITIN</td></tr>
<tr><td>Crédito</td><td>Puntaje de crédito (muchos piden alrededor de 660) o crédito alternativo: pagos de renta, luz o teléfono a tiempo</td></tr>
<tr><td>Ingresos</td><td>Comprobables y estables, normalmente dos años en el mismo trabajo o negocio</td></tr>
<tr><td>Tasa de interés</td><td>Suele estar 1 a 2 puntos por encima de un préstamo convencional</td></tr>
</tbody>
</table>

<h2>¿Cuánto dinero necesitas ahorrar?</h2>
<p>Además del enganche, aparta dinero para los costos de cierre (normalmente entre 2% y 5% del precio) y algunos meses de pagos como reserva. Un ejemplo con una casa de $600,000, cerca del precio mediano de <a href="/areas/pittsburg/">Pittsburg</a> y <a href="/areas/antioch/">Antioch</a> en 2026:</p>
<table>
<thead><tr><th>Concepto</th><th>Con 15% de enganche</th><th>Con 20% de enganche</th></tr></thead>
<tbody>
<tr><td>Enganche</td><td>$90,000</td><td>$120,000</td></tr>
<tr><td>Costos de cierre (2% a 5%)</td><td>$12,000 a $30,000</td><td>$12,000 a $30,000</td></tr>
<tr><td>Total aproximado para cerrar</td><td>$102,000 a $120,000</td><td>$132,000 a $150,000</td></tr>
</tbody>
</table>
<p>Lee más en <a href="/blog/costos-de-cierre-comprador-california/">costos de cierre al comprar casa en California</a>.</p>

<h2>¿Puedo usar programas de ayuda como CalHFA con ITIN?</h2>
<p>En general, no. Los programas de CalHFA (como MyHome y Dream For All) piden que cada comprador sea ciudadano estadounidense o "qualified alien". Si en tu familia alguien tiene número de Seguro Social y estatus que califique, revisa las opciones en <a href="/blog/programas-primera-casa-california/">programas para comprar tu primera casa en California</a>.</p>

<h2>¿Cuáles son los pasos para comprar casa con ITIN?</h2>
<ol>
<li><strong>Pon al día tus impuestos.</strong> Ten listas las declaraciones de los últimos dos años con tu ITIN.</li>
<li><strong>Revisa tu crédito.</strong> Paga a tiempo y baja tus deudas de tarjetas. Si no tienes historial, guarda comprobantes de renta y servicios.</li>
<li><strong>Ahorra en una cuenta de banco.</strong> El prestamista necesita ver de dónde viene el dinero; el efectivo sin rastro complica la aprobación.</li>
<li><strong>Habla con un prestamista que ofrezca préstamos ITIN</strong> y pide una preaprobación por escrito y un Loan Estimate para comparar costos.</li>
<li><strong>Define zona y presupuesto con tu agente.</strong> Ciudades como <a href="/areas/pittsburg/">Pittsburg</a>, <a href="/areas/antioch/">Antioch</a> o <a href="/areas/richmond/">Richmond</a> suelen ser más accesibles.</li>
<li><strong>Haz tu oferta</strong> con la carta de preaprobación.</li>
<li><strong>Inspección, tasación y cierre.</strong> El escrow normalmente dura alrededor de 30 a 45 días.</li>
</ol>

<h2>¿Qué errores debes evitar?</h2>
<ul>
<li>Depositar grandes cantidades de efectivo justo antes de pedir el préstamo sin poder explicar su origen.</li>
<li>Cambiar de trabajo, comprar un carro o abrir tarjetas nuevas durante el proceso.</li>
<li>Elegir prestamista sin comparar: pide al menos dos Loan Estimates.</li>
<li>Firmar documentos que no entiendes. Tu agente debe explicarte cada paso en tu idioma.</li>
</ul>
''',
        'faq': [
            ('¿Necesito ser ciudadano para ser dueño de una casa en California?',
             'No. En California no necesitas ser ciudadano para ser dueño de una casa. Lo que cambia según tus documentos es el tipo de préstamo al que puedes aplicar.'),
            ('¿Puedo comprar con mi pareja si uno tiene Seguro Social y el otro ITIN?',
             'Sí, es posible. Algunas parejas califican con un préstamo tradicional usando el ingreso de quien tiene Seguro Social, y otras usan un préstamo ITIN con los dos. Depende de sus ingresos y del prestamista.'),
            ('¿Puedo refinanciar un préstamo ITIN más adelante?',
             'Sí. Si mejora tu crédito o cambia tu estatus, puedes refinanciar a otro tipo de préstamo. Antes de firmar, pregunta si tu préstamo tiene penalidad por pago anticipado.'),
        ],
        'sources': [
            ('IRS: Número de Identificación Personal del Contribuyente (ITIN)', 'https://www.irs.gov/individuals/individual-taxpayer-identification-number'),
            ('Guild Mortgage: requisitos de préstamos ITIN', 'https://guildmortgage.com/itin-mortgage-loan-program-options-and-requirements'),
            ('JVM Lending: guía de préstamos ITIN', 'https://www.jvmlending.com/blog/itin-mortgage-loans-a-comprehensive-guide/'),
            ('CFPB: cómo leer tu Loan Estimate', 'https://www.consumerfinance.gov/owning-a-home/loan-estimate/'),
        ],
    },
    {
        'slug': 'programas-primera-casa-california',
        'category': 'Comprar',
        'title': 'Programas para comprar tu primera casa en California (2026): CalHFA, Dream For All y más',
        'seo_title': 'Programas para comprar tu primera casa en California (2026)',
        'desc': 'Ayuda para comprar tu primera casa en California en 2026: CalHFA MyHome (hasta 3.5%), ZIP para costos de cierre, Dream For All y préstamos con 3% o 3.5% de enganche.',
        'keywords': ['programas primera casa California', 'CalHFA 2026', 'Dream For All 2026', 'ayuda para el enganche California'],
        'cities': ['oakland', 'concord', 'hayward', 'san-francisco'],
        'related': ['cuanto-enganche-para-comprar-casa-california', 'comprar-casa-con-itin-california', 'costos-de-cierre-comprador-california'],
        'answer': 'Los principales programas estatales son de CalHFA. MyHome presta hasta 3.5% del precio (con préstamo FHA) o 3% (convencional) para el enganche, y ZIP ayuda con los costos de cierre; los dos son préstamos diferidos que pagas al vender o refinanciar. Dream For All cubre hasta 20% del precio (máximo $150,000), pero funciona por rondas y sorteo: la de 2026 cerró en marzo.',
        'body': '''
<h2>¿Quién cuenta como comprador de primera vivienda?</h2>
<p>Para CalHFA y la mayoría de los programas, eres "primer comprador" si no has sido dueño de la casa en la que viviste durante los últimos tres años. Si vendiste una casa hace más de tres años, es posible que vuelvas a calificar.</p>

<h2>¿Qué programas de CalHFA hay en 2026?</h2>
<table>
<thead><tr><th>Programa</th><th>Qué cubre</th><th>Cómo se paga</th></tr></thead>
<tbody>
<tr><td>MyHome Assistance</td><td>Hasta 3.5% del precio con préstamo FHA o 3% con préstamo convencional</td><td>Préstamo diferido: no pagas mensualidad; se paga al vender, refinanciar o terminar la hipoteca</td></tr>
<tr><td>ZIP (Zero Interest Program)</td><td>Costos de cierre</td><td>Préstamo diferido sin intereses</td></tr>
<tr><td>Dream For All</td><td>Hasta 20% del precio, con máximo de $150,000, para compradores de primera generación</td><td>Préstamo de apreciación compartida: devuelves el monto más un porcentaje de lo que suba el valor de la casa</td></tr>
</tbody>
</table>
<p>Todos se usan junto con un primer préstamo de CalHFA y a través de un prestamista aprobado por CalHFA.</p>

<h2>¿Qué requisitos piden?</h2>
<ul>
<li>Ser comprador de primera vivienda y vivir en la casa.</li>
<li>Tomar un curso de educación para compradores (el certificado vale un año).</li>
<li>Estar dentro de los límites de ingreso y de precio de tu condado.</li>
<li>Ser ciudadano estadounidense o "qualified alien". Con solo ITIN normalmente no se califica; mira <a href="/blog/comprar-casa-con-itin-california/">cómo comprar casa con ITIN</a>.</li>
<li>Cumplir el puntaje de crédito mínimo del préstamo que uses.</li>
</ul>

<h2>¿Cuándo abre Dream For All?</h2>
<p>Dream For All no está abierto todo el año. En 2026 CalHFA abrió solicitudes a principios de año, cerró el 16 de marzo de 2026 y asignó los certificados por sorteo. Si te interesa la próxima ronda, prepárate antes: termina el curso para compradores y consigue tu preaprobación para estar listo cuando CalHFA la anuncie.</p>

<h2>¿Qué préstamos permiten poco enganche?</h2>
<ul>
<li><strong>FHA:</strong> desde 3.5% de enganche con puntaje de 580 o más.</li>
<li><strong>Convencional para primeros compradores:</strong> desde 3% en programas como HomeReady o Home Possible.</li>
<li><strong>VA:</strong> 0% de enganche para veteranos y militares que califican.</li>
</ul>
<p>En 2026, el límite del préstamo convencional (conforming) en Alameda, Contra Costa y San Francisco es de $1,249,125. Verifica el límite FHA de tu condado en la herramienta de HUD. Más detalles en <a href="/blog/cuanto-enganche-para-comprar-casa-california/">cuánto enganche necesitas</a>.</p>

<h2>Ejemplo: casa de $650,000 con FHA y MyHome</h2>
<table>
<thead><tr><th>Concepto</th><th>Monto</th></tr></thead>
<tbody>
<tr><td>Enganche FHA (3.5%)</td><td>$22,750</td></tr>
<tr><td>MyHome (hasta 3.5% del precio)</td><td>Hasta $22,750</td></tr>
<tr><td>Costos de cierre</td><td>Puede ayudarte ZIP; el resto lo pagas tú o lo negocias con el vendedor</td></tr>
</tbody>
</table>
<p>Con esta combinación, el enganche puede salir casi en su totalidad del programa. A cambio, tendrás un segundo préstamo que pagarás cuando vendas o refinancies.</p>

<h2>¿Hay programas de tu ciudad?</h2>
<p>Algunas ciudades, como <a href="/areas/san-francisco/">San Francisco</a> a través de su Oficina de Vivienda (MOHCD) y <a href="/areas/oakland/">Oakland</a>, han ofrecido programas propios para primeros compradores. Los fondos y requisitos cambian cada año, así que pregunta por ellos antes de empezar a buscar casa.</p>

<h2>¿Cómo aplicas paso a paso?</h2>
<ol>
<li>Toma el curso de educación para compradores.</li>
<li>Busca un prestamista aprobado por CalHFA y pide tu preaprobación con el programa.</li>
<li>Busca casas dentro del límite de precio de tu condado.</li>
<li>Haz tu oferta indicando que usarás asistencia de CalHFA.</li>
</ol>
''',
        'faq': [
            ('¿Tengo que devolver la ayuda de CalHFA?',
             'Sí. MyHome y ZIP son préstamos diferidos: no pagas mensualidades, pero los devuelves al vender, refinanciar o terminar de pagar tu hipoteca. Dream For All se devuelve con una parte de la plusvalía de la casa.'),
            ('¿Puedo usar CalHFA si compro en cualquier ciudad del Bay Area?',
             'Sí, CalHFA funciona en todo California, pero los límites de ingreso y de precio cambian según el condado.'),
            ('¿Cuándo será la próxima ronda de Dream For All?',
             'CalHFA la anuncia en su sitio web. En 2026 la ronda abrió a principios de año y cerró el 16 de marzo, así que conviene estar preparado desde el inicio del año.'),
        ],
        'sources': [
            ('CalHFA: programas para compradores', 'https://www.calhfa.ca.gov/homebuyer/'),
            ('CalHFA: MyHome Assistance Program (PDF)', 'https://www.calhfa.ca.gov/homeownership/programs/myhome.pdf'),
            ('FHFA: límites de préstamo 2026', 'https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026'),
            ('HUD: límites de préstamo FHA por condado', 'https://entp.hud.gov/idapp/html/hicostlook.cfm'),
            ('The Mortgage Reports: Dream For All 2026', 'https://themortgagereports.com/112152/california-first-time-home-buyers-dream-for-all-loan'),
        ],
    },
    {
        'slug': 'cuanto-enganche-para-comprar-casa-california',
        'category': 'Comprar',
        'title': '¿Cuánto enganche necesitas para comprar casa en California? (2026)',
        'seo_title': '¿Cuánto enganche necesitas para comprar casa en California? (2026)',
        'desc': 'Desde 3% con préstamo convencional, 3.5% con FHA y 0% con VA. Cuánto enganche necesitas en California en 2026, cuándo pagas PMI y ejemplos con casas de $600,000 a $900,000.',
        'keywords': ['cuánto enganche para comprar casa', 'down payment California', 'enganche FHA', 'PMI'],
        'cities': ['concord', 'brentwood', 'hayward'],
        'related': ['programas-primera-casa-california', 'costos-de-cierre-comprador-california', 'casas-mas-baratas-bay-area-east-bay'],
        'answer': 'Menos de lo que mucha gente cree: desde 3% con un préstamo convencional para primeros compradores, 3.5% con FHA (puntaje de 580 o más) y 0% con VA para veteranos. Con 20% evitas el seguro hipotecario privado (PMI) en un préstamo convencional. Además del enganche, aparta entre 2% y 5% del precio para costos de cierre.',
        'body': '''
<h2>¿Cuánto enganche pide cada tipo de préstamo?</h2>
<table>
<thead><tr><th>Préstamo</th><th>Enganche mínimo</th><th>Lo que debes saber</th></tr></thead>
<tbody>
<tr><td>Convencional</td><td>3% a 5%</td><td>3% en programas para primeros compradores; con menos de 20% pagas PMI</td></tr>
<tr><td>FHA</td><td>3.5%</td><td>Con puntaje de 580 o más (10% si tienes entre 500 y 579); tiene seguro hipotecario (MIP)</td></tr>
<tr><td>VA</td><td>0%</td><td>Para veteranos y militares que califican</td></tr>
<tr><td>Jumbo</td><td>Normalmente 10% a 20%</td><td>Préstamos mayores a $1,249,125 en el Bay Area en 2026</td></tr>
<tr><td>ITIN</td><td>Normalmente 15% a 20%</td><td>Ver <a href="/blog/comprar-casa-con-itin-california/">comprar casa con ITIN</a></td></tr>
</tbody>
</table>

<h2>¿Cuánto es en dólares?</h2>
<table>
<thead><tr><th>Precio de la casa</th><th>3%</th><th>3.5%</th><th>10%</th><th>20%</th></tr></thead>
<tbody>
<tr><td>$600,000</td><td>$18,000</td><td>$21,000</td><td>$60,000</td><td>$120,000</td></tr>
<tr><td>$750,000</td><td>$22,500</td><td>$26,250</td><td>$75,000</td><td>$150,000</td></tr>
<tr><td>$900,000</td><td>$27,000</td><td>$31,500</td><td>$90,000</td><td>$180,000</td></tr>
</tbody>
</table>
<p>Como referencia, en 2026 las casas en <a href="/areas/concord/">Concord</a> y <a href="/areas/brentwood/">Brentwood</a> rondan los $750,000, y en <a href="/areas/hayward/">Hayward</a> los $850,000 (precio mediano, según Redfin).</p>

<h2>¿Qué es el PMI y cuándo lo pagas?</h2>
<p>El PMI (seguro hipotecario privado) protege al banco si das menos de 20% en un préstamo convencional. Se suma a tu pago mensual, pero no es para siempre: puedes pedir que lo quiten cuando debas 80% del valor original de la casa, y se cancela automáticamente al llegar a 78%.</p>
<p>En FHA el seguro se llama MIP: hay una prima inicial de 1.75% del préstamo (se puede financiar) y una prima anual. Si das menos de 10%, la prima anual dura toda la vida del préstamo; si das 10% o más, dura 11 años.</p>

<h2>¿Conviene dar 20%?</h2>
<p>No siempre. Dar 20% baja tu pago y elimina el PMI, pero juntar ese dinero en el Bay Area puede tomar años mientras los precios siguen cambiando. Muchas familias compran con 3% a 10% y refinancian después. Lo importante es que el pago mensual total te quede cómodo y que te quede un fondo de emergencia.</p>

<h2>¿De dónde puede salir el dinero del enganche?</h2>
<ul>
<li>Ahorros en tu cuenta (los prestamistas suelen pedir los estados de cuenta de los últimos dos meses).</li>
<li>Un regalo de un familiar, con una carta de regalo firmada.</li>
<li>Programas de asistencia como <a href="/blog/programas-primera-casa-california/">CalHFA MyHome</a>.</li>
<li>Un préstamo de tu plan de retiro 401(k), si tu plan lo permite.</li>
</ul>

<h2>¿Qué otros gastos hay además del enganche?</h2>
<p>Los costos de cierre suelen sumar entre 2% y 5% del precio, y además deberás dar un depósito de buena fe (earnest money) al aceptar tu oferta, que luego se abona al enganche. Lee la guía de <a href="/blog/costos-de-cierre-comprador-california/">costos de cierre en California</a>.</p>
''',
        'faq': [
            ('¿Puedo comprar casa en California sin enganche?',
             'Sí, con un préstamo VA si eres veterano o militar que califica. Otra opción es combinar un préstamo FHA o convencional con un programa de asistencia como CalHFA MyHome, que puede cubrir el enganche mínimo.'),
            ('¿Puedo usar dinero que me regala mi familia?',
             'Sí. FHA y los préstamos convencionales aceptan regalos de familiares con una carta de regalo y comprobantes de dónde salió el dinero.'),
            ('¿Pierdo mi depósito si la compra no se cierra?',
             'Depende del motivo. Si cancelas dentro de tus contingencias (inspección, tasación o préstamo), normalmente lo recuperas. Si incumples el contrato sin una contingencia vigente, podrías perderlo. En California, la cláusula de daños liquidados limita esa pérdida a 3% del precio.'),
        ],
        'sources': [
            ('HUD: préstamos FHA', 'https://www.hud.gov/buying/loans'),
            ('CFPB: qué es el seguro hipotecario privado (PMI)', 'https://www.consumerfinance.gov/ask-cfpb/what-is-private-mortgage-insurance-en-122/'),
            ('VA: préstamos para vivienda', 'https://www.va.gov/housing-assistance/home-loans/'),
            ('FHFA: límites de préstamo 2026', 'https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026'),
        ],
    },
    {
        'slug': 'costos-de-cierre-comprador-california',
        'category': 'Comprar',
        'title': 'Costos de cierre al comprar casa en California (2026): cuánto son y qué incluyen',
        'seo_title': 'Costos de cierre al comprar casa en California (2026)',
        'desc': 'Los costos de cierre para el comprador en California suelen ser de 2% a 5% del precio. Qué incluyen, quién paga qué, el impuesto de transferencia y cómo reducirlos.',
        'keywords': ['costos de cierre California', 'closing costs comprador', 'escrow California', 'impuesto de transferencia'],
        'cities': ['oakland', 'san-leandro', 'walnut-creek'],
        'related': ['cuanto-enganche-para-comprar-casa-california', 'programas-primera-casa-california', 'cuanto-cuesta-vender-casa-california'],
        'answer': 'Para el comprador, los costos de cierre en California suelen sumar entre 2% y 5% del precio de compra. Incluyen cargos del préstamo, tasación, escrow, seguro de título, impuestos y seguro prepagados y, a veces, parte del impuesto de transferencia. En una casa de $700,000, eso puede ser de $14,000 a $35,000.',
        'body': '''
<h2>¿Qué incluyen los costos de cierre?</h2>
<table>
<thead><tr><th>Costo</th><th>Qué es</th></tr></thead>
<tbody>
<tr><td>Cargos del préstamo</td><td>Origination fee, puntos (si compras una tasa más baja) y procesamiento</td></tr>
<tr><td>Tasación (appraisal)</td><td>El avalúo que pide el banco para confirmar el valor de la casa</td></tr>
<tr><td>Escrow</td><td>La compañía neutral que guarda el dinero y coordina el cierre</td></tr>
<tr><td>Seguro de título</td><td>Protege contra problemas con la propiedad legal de la casa</td></tr>
<tr><td>Prepagados</td><td>Intereses de los primeros días, seguro de la casa y meses de impuestos para la cuenta de reserva</td></tr>
<tr><td>Registro y notario</td><td>Cargos del condado por registrar la escritura y el préstamo</td></tr>
<tr><td>Inspecciones</td><td>Inspección general y de termitas; se pagan antes del cierre</td></tr>
</tbody>
</table>

<h2>¿Quién paga el impuesto de transferencia?</h2>
<p>Todos los condados de California cobran $1.10 por cada $1,000 del precio. Algunas ciudades cobran un impuesto adicional: en <a href="/areas/oakland/">Oakland</a>, por ejemplo, la tasa va de 1% (casas de hasta $300,000) a 1.5% (de $300,001 a $2 millones). La ley no dice quién lo paga; se negocia en el contrato y depende de la costumbre local. Pregunta a tu agente cómo se acostumbra en la ciudad donde compras.</p>

<h2>¿Cuánto es en una casa de $700,000?</h2>
<table>
<thead><tr><th>Escenario</th><th>Costos de cierre aproximados</th></tr></thead>
<tbody>
<tr><td>Bajo (2%)</td><td>$14,000</td></tr>
<tr><td>Medio (3.5%)</td><td>$24,500</td></tr>
<tr><td>Alto (5%)</td><td>$35,000</td></tr>
</tbody>
</table>

<h2>¿Cuándo sabes el monto exacto?</h2>
<p>Tres días hábiles después de solicitar el préstamo recibes un <strong>Loan Estimate</strong> con los costos estimados. Al menos tres días hábiles antes de firmar recibes el <strong>Closing Disclosure</strong> con los montos finales. Compara los dos documentos y pregunta por cualquier diferencia.</p>

<h2>¿Cómo puedes pagar menos?</h2>
<ul>
<li><strong>Créditos del vendedor:</strong> puedes negociar que el vendedor pague parte de tus costos. FHA permite hasta 6% del precio; en préstamos convencionales el máximo depende de tu enganche.</li>
<li><strong>Créditos del prestamista:</strong> aceptas una tasa un poco más alta a cambio de que el banco pague parte de los costos.</li>
<li><strong>Programas de asistencia:</strong> el programa ZIP de CalHFA ayuda con costos de cierre. Lee sobre <a href="/blog/programas-primera-casa-california/">programas para primeros compradores</a>.</li>
<li><strong>Comparar prestamistas:</strong> pide dos o tres Loan Estimates el mismo día y compáralos línea por línea.</li>
</ul>

<h2>¿Qué gastos llegan después del cierre?</h2>
<p>En California, al comprar se vuelve a valorar la casa para los impuestos (Proposición 13). Unos meses después del cierre suele llegar una <strong>factura suplementaria de impuestos</strong> por la diferencia entre el valor anterior y tu precio de compra. Aparta dinero para pagarla.</p>
<p>También considera el seguro contra terremotos, que en California se compra por separado. La California Earthquake Authority ofrece pólizas a través de las aseguradoras.</p>
''',
        'faq': [
            ('¿Los costos de cierre se pueden incluir en el préstamo?',
             'Normalmente no se suman al préstamo en una compra, pero puedes reducirlos con créditos del vendedor o del prestamista. En FHA, la prima inicial de seguro (1.75%) sí se puede financiar.'),
            ('¿Qué es el escrow en California?',
             'Es una compañía neutral que guarda el depósito y los fondos, recibe los documentos del comprador, del vendedor y del banco, y entrega el dinero y la escritura cuando se cumplen todas las condiciones del contrato.'),
            ('¿Cuánto tarda el cierre?',
             'Con préstamo, el escrow suele durar alrededor de 30 a 45 días. Una compra en efectivo puede cerrar más rápido.'),
        ],
        'sources': [
            ('CFPB: el Closing Disclosure', 'https://www.consumerfinance.gov/owning-a-home/closing-disclosure/'),
            ('CFPB: el Loan Estimate', 'https://www.consumerfinance.gov/owning-a-home/loan-estimate/'),
            ('Ciudad de Oakland: impuesto de transferencia', 'https://www.oaklandca.gov/resources/real-estate-transfer-tax'),
            ('California Earthquake Authority', 'https://www.earthquakeauthority.com/'),
        ],
    },
    {
        'slug': 'cuanto-cuesta-vender-casa-california',
        'category': 'Vender',
        'title': '¿Cuánto cuesta vender una casa en California? Comisiones, impuestos y costos (2026)',
        'seo_title': '¿Cuánto cuesta vender una casa en California? (2026)',
        'desc': 'Qué pagas al vender tu casa en California en 2026: comisiones negociables, impuesto de transferencia, escrow, reparaciones e impuestos sobre la ganancia. Con ejemplo en Oakland.',
        'keywords': ['cuánto cuesta vender una casa', 'costos de venta California', 'comisión realtor', 'impuesto ganancia venta casa'],
        'cities': ['oakland', 'hayward', 'richmond'],
        'related': ['como-vender-tu-casa-bay-area', 'cuanto-vale-mi-casa-bay-area', 'que-hace-un-realtor-cuanto-cobra-california'],
        'answer': 'Vender una casa en California suele costar entre 6% y 10% del precio final. La mayor parte son comisiones, que son negociables. El resto es impuesto de transferencia, escrow y título, reparaciones o créditos al comprador y la preparación de la casa. Si fue tu residencia principal 2 de los últimos 5 años, puedes excluir hasta $250,000 de ganancia ($500,000 si son casados) del impuesto federal.',
        'body': '''
<h2>¿Qué costos pagas al vender?</h2>
<table>
<thead><tr><th>Costo</th><th>Qué debes saber</th></tr></thead>
<tbody>
<tr><td>Comisiones</td><td>No hay una tarifa fija: se negocian con tu agente. Tú decides si ofreces compensación al agente del comprador.</td></tr>
<tr><td>Impuesto de transferencia</td><td>$1.10 por cada $1,000 en el condado, más el impuesto de algunas ciudades</td></tr>
<tr><td>Escrow y título</td><td>Se dividen según la costumbre del condado y lo que se negocie</td></tr>
<tr><td>Reparaciones o créditos</td><td>Lo que acuerdes después de la inspección del comprador</td></tr>
<tr><td>Preparación</td><td>Pintura, limpieza, jardín, staging y fotos profesionales</td></tr>
<tr><td>Otros</td><td>Impuestos de la propiedad prorrateados, cuotas de HOA y el saldo de tu hipoteca</td></tr>
</tbody>
</table>

<h2>¿Cómo funcionan las comisiones desde 2024?</h2>
<p>Desde agosto de 2024 las ofertas de compensación ya no aparecen en el MLS, y el comprador firma su propio acuerdo con su agente. Como vendedor, puedes ofrecer pagar parte o toda la comisión del agente del comprador para atraer más ofertas, pero no es obligatorio. Todo se negocia. Más detalles en <a href="/blog/que-hace-un-realtor-cuanto-cobra-california/">qué hace un realtor y cuánto cobra</a>.</p>

<h2>Ejemplo: vender una casa de $750,000 en Oakland</h2>
<table>
<thead><tr><th>Concepto</th><th>Monto aproximado</th></tr></thead>
<tbody>
<tr><td>Cada 1% de comisión</td><td>$7,500</td></tr>
<tr><td>Impuesto del condado ($1.10 por $1,000)</td><td>$825</td></tr>
<tr><td>Impuesto de la ciudad de Oakland (1.5%)</td><td>$11,250 (quién lo paga se negocia)</td></tr>
<tr><td>Escrow, título y otros cargos</td><td>Varios miles de dólares, según el contrato</td></tr>
</tbody>
</table>
<p>Ciudades como <a href="/areas/oakland/">Oakland</a>, San Francisco, Berkeley, <a href="/areas/richmond/">Richmond</a>, <a href="/areas/hayward/">Hayward</a> y <a href="/areas/san-leandro/">San Leandro</a> tienen su propio impuesto de transferencia, y otras ciudades no. Verifica la tarifa de tu ciudad antes de calcular tu ganancia.</p>

<h2>¿Pagas impuestos por la ganancia?</h2>
<p>Si la casa fue tu residencia principal al menos 2 de los últimos 5 años, puedes excluir hasta $250,000 de ganancia del impuesto federal, o $500,000 si son casados y declaran juntos. California no tiene una tasa especial para ganancias de capital: lo que no quede excluido se suma a tus ingresos normales. Si la casa era de inversión o la tuviste poco tiempo, habla con un contador antes de vender.</p>

<h2>¿Cómo puedes reducir tus costos?</h2>
<ul>
<li>Negocia la comisión y los servicios incluidos antes de firmar el contrato de venta.</li>
<li>Haz inspecciones antes de publicar para evitar sorpresas y créditos grandes después.</li>
<li>Arregla lo pequeño y visible: suele costar menos que un descuento en el precio.</li>
<li>Pon un precio correcto desde el inicio; una casa que se queda semanas en el mercado termina vendiéndose con descuento. Lee <a href="/blog/cuanto-vale-mi-casa-bay-area/">cómo saber cuánto vale tu casa</a>.</li>
</ul>
''',
        'faq': [
            ('¿Tengo que pagar la comisión del agente del comprador?',
             'No es obligatorio. Desde 2024 el comprador tiene su propio acuerdo con su agente. Como vendedor puedes ofrecer pagar parte de esa comisión para atraer más compradores; es una decisión de estrategia que se negocia.'),
            ('¿Cuándo recibo el dinero de la venta?',
             'Al cerrar el escrow. La compañía de escrow paga tu hipoteca y los costos, y te envía el resto, normalmente por transferencia, el mismo día del cierre o pocos días después.'),
            ('¿Puedo vender si todavía debo mucho de mi hipoteca?',
             'Sí. El saldo se paga con el dinero de la venta. Si debes más de lo que vale la casa, existen opciones como una venta corta (short sale), que requiere aprobación del banco.'),
        ],
        'sources': [
            ('IRS: Tema 701, venta de su vivienda', 'https://www.irs.gov/taxtopics/tc701'),
            ('Ciudad de Oakland: impuesto de transferencia', 'https://www.oaklandca.gov/resources/real-estate-transfer-tax'),
            ('California DRE: cambios en la representación inmobiliaria', 'https://www.dre.ca.gov/Consumers/ConsumerAlert_20241114_Changes_to_Real_Estate_Representation.html'),
            ('NAR: datos sobre el acuerdo de comisiones', 'https://www.nar.realtor/the-facts'),
        ],
    },
    {
        'slug': 'como-vender-tu-casa-bay-area',
        'category': 'Vender',
        'title': 'Cómo vender tu casa en el Bay Area: 9 pasos para venderla rápido y al mejor precio (2026)',
        'seo_title': 'Cómo vender tu casa en el Bay Area: 9 pasos (2026)',
        'desc': 'Guía paso a paso para vender tu casa en el Bay Area en 2026: precio, preparación, inspecciones, divulgaciones obligatorias en California, ofertas y cierre.',
        'keywords': ['cómo vender mi casa', 'vender casa Bay Area', 'vender casa rápido', 'divulgaciones vendedor California'],
        'cities': ['oakland', 'walnut-creek', 'concord'],
        'related': ['cuanto-cuesta-vender-casa-california', 'cuanto-vale-mi-casa-bay-area', 'que-hace-un-realtor-cuanto-cobra-california'],
        'answer': 'Para vender bien en el Bay Area: fija el precio con un análisis comparativo de mercado, prepara la casa (reparaciones pequeñas, limpieza y staging), haz inspecciones antes de publicar, entrega las divulgaciones que exige California, publica con fotos profesionales y compara las ofertas no solo por precio sino por contingencias y plazo de cierre.',
        'body': '''
<h2>1. ¿Cuánto vale tu casa hoy?</h2>
<p>Empieza con un análisis comparativo de mercado (CMA) con ventas recientes cerca de tu casa. Un precio correcto desde el primer día atrae más compradores; un precio alto hace que la casa se quede en el mercado y termine vendiéndose por menos. Lee <a href="/blog/cuanto-vale-mi-casa-bay-area/">cómo se calcula el valor de tu casa</a>.</p>

<h2>2. ¿Qué arreglos valen la pena?</h2>
<p>Enfócate en lo que el comprador ve y en lo que saldría en una inspección: pintura, luces, llaves que gotean, puertas que no cierran y jardín. Las remodelaciones grandes justo antes de vender casi nunca recuperan lo que cuestan.</p>

<h2>3. ¿Conviene hacer inspecciones antes de publicar?</h2>
<p>En el Bay Area es muy común. Una inspección general y una de termitas (pest) te dicen qué hay que reparar y le dan confianza al comprador. Así negocias desde el inicio y no después de aceptar una oferta.</p>

<h2>4. ¿Qué divulgaciones exige California?</h2>
<ul>
<li><strong>Transfer Disclosure Statement (TDS):</strong> el estado de la casa según el vendedor.</li>
<li><strong>Natural Hazard Disclosure (NHD):</strong> zonas de riesgo como inundación, incendio o fallas sísmicas.</li>
<li><strong>Pintura con plomo:</strong> obligatoria para casas construidas antes de 1978.</li>
<li><strong>Detectores y calentador:</strong> detectores de humo y monóxido de carbono, y el calentador de agua sujetado con correas sísmicas.</li>
</ul>
<p>Además, en <a href="/areas/oakland/">Oakland</a> y otras ciudades del East Bay servidas por EBMUD, al vender necesitas un certificado de cumplimiento de la tubería de drenaje privada (sewer lateral).</p>

<h2>5. ¿Cómo preparas la casa para las fotos?</h2>
<p>Limpieza profunda, menos muebles, nada personal a la vista y luz natural. El staging (amueblar o decorar para vender) ayuda a que el comprador se imagine viviendo ahí, sobre todo en casas vacías.</p>

<h2>6. ¿Dónde se promociona la casa?</h2>
<p>En el MLS, que alimenta Zillow, Redfin y Realtor.com, más redes sociales, open houses y la red de agentes de la zona. Las fotos y el primer fin de semana son lo más importante.</p>

<h2>7. ¿Cuál es la mejor estrategia de precio y ofertas?</h2>
<p>Hay dos estrategias comunes: un precio de lista ajustado con fecha para recibir ofertas (para generar competencia), o un precio cercano al valor real para vender rápido sin regateo. Depende del barrio y de la temporada; en ciudades como <a href="/areas/walnut-creek/">Walnut Creek</a> la competencia suele ser mayor.</p>

<h2>8. ¿Cómo comparas las ofertas?</h2>
<table>
<thead><tr><th>Mira esto</th><th>Por qué importa</th></tr></thead>
<tbody>
<tr><td>Precio</td><td>Lo más visible, pero no lo único</td></tr>
<tr><td>Contingencias</td><td>Inspección, tasación y préstamo: menos contingencias significa menos riesgo de que se caiga la venta</td></tr>
<tr><td>Tipo de préstamo y enganche</td><td>Un comprador con más enganche o en efectivo es más seguro</td></tr>
<tr><td>Fecha de cierre</td><td>Que se ajuste a tu mudanza</td></tr>
<tr><td>Créditos que pide</td><td>Un precio alto con muchos créditos puede dejarte menos dinero</td></tr>
</tbody>
</table>

<h2>9. ¿Qué pasa en el escrow y el cierre?</h2>
<p>Después de aceptar la oferta, el comprador hace su depósito, sus inspecciones y la tasación, y se levantan las contingencias. El escrow suele durar alrededor de 30 a 45 días. Al cierre se paga tu hipoteca y recibes el resto. Calcula cuánto te quedará con la guía de <a href="/blog/cuanto-cuesta-vender-casa-california/">cuánto cuesta vender una casa</a>.</p>
''',
        'faq': [
            ('¿Conviene vender la casa "as is" (como está)?',
             'Puede convenir si no tienes tiempo o dinero para reparar. Vas a recibir menos ofertas y más bajas, pero ahorras en arreglos. Aun vendiendo "as is" debes entregar todas las divulgaciones.'),
            ('¿Cuál es la mejor época para vender en el Bay Area?',
             'La primavera suele traer más compradores, pero también más casas a la venta. Una casa bien preparada y con buen precio se vende en cualquier temporada.'),
            ('¿Tengo que arreglar todo lo que salga en la inspección del comprador?',
             'No. Lo que salga se negocia: puedes reparar, dar un crédito, bajar el precio o no aceptar. Por eso ayudan las inspecciones antes de publicar.'),
        ],
        'sources': [
            ('EBMUD: programa de tuberías de drenaje privadas (sewer lateral)', 'https://www.ebmud.com/wastewater/private-sewer-laterals'),
            ('EPA: divulgación de pintura con plomo', 'https://www.epa.gov/lead/real-estate-disclosure'),
            ('California DRE: información para consumidores', 'https://www.dre.ca.gov/Consumers/'),
        ],
    },
    {
        'slug': 'cuanto-vale-mi-casa-bay-area',
        'category': 'Vender',
        'title': '¿Cuánto vale mi casa? Cómo saber el precio real de tu casa en el Bay Area (2026)',
        'seo_title': '¿Cuánto vale mi casa? Precio real en el Bay Area (2026)',
        'desc': 'Cómo se calcula el valor de tu casa en el Bay Area: análisis comparativo (CMA), tasación y estimados en línea. Qué sube o baja el precio y medianas de 2026 por ciudad.',
        'keywords': ['cuánto vale mi casa', 'valor de mi casa', 'CMA', 'Zestimate', 'precio de casas Bay Area 2026'],
        'cities': ['oakland', 'san-leandro', 'hayward', 'walnut-creek'],
        'related': ['como-vender-tu-casa-bay-area', 'cuanto-cuesta-vender-casa-california', 'casas-mas-baratas-bay-area-east-bay'],
        'answer': 'Tu casa vale lo que los compradores están pagando hoy por casas parecidas cerca de la tuya. La forma más precisa de saberlo es un análisis comparativo de mercado (CMA) con ventas de los últimos 3 a 6 meses, ajustadas por tamaño, estado y ubicación. Los estimados automáticos como el Zestimate sirven de referencia, pero en el Bay Area pueden equivocarse por decenas de miles de dólares.',
        'body': '''
<h2>¿Qué hace que una casa valga más o menos?</h2>
<ul>
<li><strong>Ubicación:</strong> el barrio, la calle, las escuelas y la cercanía al BART o a las autopistas.</li>
<li><strong>Tamaño:</strong> pies cuadrados, recámaras, baños y tamaño del terreno.</li>
<li><strong>Estado:</strong> cocina y baños actualizados, techo, ventanas, plomería y electricidad.</li>
<li><strong>Permisos:</strong> una ampliación o un cuarto extra sin permisos puede no contar en el valor y asustar a los compradores.</li>
<li><strong>Extras:</strong> vista, estacionamiento, patio, paneles solares y espacio para una unidad adicional (ADU).</li>
</ul>

<h2>¿CMA, tasación o Zestimate: cuál es más exacto?</h2>
<table>
<thead><tr><th>Método</th><th>Quién lo hace</th><th>Para qué sirve</th></tr></thead>
<tbody>
<tr><td>Análisis comparativo de mercado (CMA)</td><td>Un agente con datos del MLS</td><td>Definir el precio de venta con ventas reales cercanas y el estado de tu casa</td></tr>
<tr><td>Tasación (appraisal)</td><td>Un tasador con licencia</td><td>Lo pide el banco del comprador para aprobar el préstamo</td></tr>
<tr><td>Estimados en línea</td><td>Algoritmos (Zillow, Redfin)</td><td>Una referencia rápida; no ven el interior ni las mejoras de tu casa</td></tr>
</tbody>
</table>

<h2>¿Cómo están los precios en 2026?</h2>
<p>Precio mediano de venta de todos los tipos de casa, según el dato más reciente de Redfin para cada ciudad:</p>
<table>
<thead><tr><th>Ciudad</th><th>Precio mediano aproximado</th><th>Dato de</th></tr></thead>
<tbody>
<tr><td><a href="/areas/pittsburg/">Pittsburg</a></td><td>$590,000</td><td>septiembre de 2026</td></tr>
<tr><td><a href="/areas/antioch/">Antioch</a></td><td>$592,000</td><td>julio a septiembre de 2026</td></tr>
<tr><td><a href="/areas/concord/">Concord</a></td><td>$758,000</td><td>junio a agosto de 2026</td></tr>
<tr><td><a href="/areas/oakland/">Oakland</a></td><td>$773,000</td><td>julio a septiembre de 2026</td></tr>
<tr><td><a href="/areas/walnut-creek/">Walnut Creek</a></td><td>$848,000</td><td>septiembre de 2026</td></tr>
<tr><td><a href="/areas/hayward/">Hayward</a></td><td>$849,000</td><td>junio a agosto de 2026</td></tr>
<tr><td><a href="/areas/san-leandro/">San Leandro</a></td><td>$870,000</td><td>marzo a mayo de 2026</td></tr>
</tbody>
</table>
<p>La mediana mezcla casas y condominios de toda la ciudad. El valor de tu casa puede estar muy por encima o por debajo; por eso el CMA usa ventas de tu barrio.</p>

<h2>¿Qué información necesito para un CMA?</h2>
<ul>
<li>Dirección, pies cuadrados, recámaras y baños.</li>
<li>Mejoras que hiciste y en qué año (techo, cocina, baños, ventanas).</li>
<li>Si hay trabajos sin permiso o reparaciones pendientes.</li>
<li>Fotos actuales del interior.</li>
</ul>

<h2>¿Qué mejoras suben el valor antes de vender?</h2>
<p>Las que cuestan poco y se ven mucho: pintura en colores neutros, luces nuevas, jardín cuidado, limpieza profunda y reparar lo que esté roto. Antes de una remodelación grande, compara su costo con lo que realmente sube el precio en tu barrio. Más en <a href="/blog/como-vender-tu-casa-bay-area/">cómo vender tu casa en el Bay Area</a>.</p>
''',
        'faq': [
            ('¿Qué tan exacto es el Zestimate?',
             'Es una estimación automática. Funciona mejor en casas recién vendidas y en barrios con casas parecidas. Como no ve el interior ni las mejoras, en el Bay Area puede quedar lejos del precio real.'),
            ('¿Cuál es la diferencia entre una tasación y un CMA?',
             'La tasación la hace un tasador con licencia para el banco del comprador. El CMA lo hace un agente para fijar el precio de venta. Los dos usan ventas comparables, pero con objetivos distintos.'),
            ('¿Un cuarto agregado sin permisos baja el valor?',
             'Puede bajarlo. Muchos compradores y tasadores no cuentan los pies cuadrados sin permiso, y algunos bancos ponen condiciones. A veces conviene legalizarlo antes de vender.'),
        ],
        'sources': [
            ('Redfin: mercado de vivienda de Oakland', 'https://www.redfin.com/city/13654/CA/Oakland/housing-market'),
            ('Redfin: mercado de vivienda de Pittsburg', 'https://www.redfin.com/city/14890/CA/Pittsburg/housing-market'),
            ('Redfin: mercado de vivienda de Walnut Creek', 'https://www.redfin.com/city/20635/CA/Walnut-Creek/housing-market'),
            ('Zillow: qué es el Zestimate', 'https://www.zillow.com/z/zestimate/'),
        ],
    },
    {
        'slug': 'fix-and-flip-bay-area-regla-70',
        'category': 'Invertir',
        'title': 'Fix & Flip en el Bay Area: cómo saber si una casa es buena inversión (regla del 70%)',
        'seo_title': 'Fix & Flip en el Bay Area: la regla del 70% explicada',
        'desc': 'Cómo calcular un Fix & Flip en el Bay Area: la regla del 70%, el valor después de reparar (ARV), costos ocultos, financiamiento, permisos e impuestos. Con ejemplo en Oakland.',
        'keywords': ['fix and flip', 'regla del 70%', 'invertir en casas Bay Area', 'ARV', 'remodelar y vender casa'],
        'cities': ['oakland', 'antioch', 'richmond'],
        'related': ['cuanto-vale-mi-casa-bay-area', 'cuanto-cuesta-vender-casa-california', 'casas-mas-baratas-bay-area-east-bay'],
        'answer': 'La regla del 70% dice que no debes pagar más del 70% del valor de reventa (ARV) menos el costo de las reparaciones. Si una casa se venderá en $900,000 ya remodelada y necesita $120,000 de obra, tu precio máximo sería $900,000 × 0.70 − $120,000 = $510,000. En el Bay Area es un filtro inicial: también debes sumar financiamiento, permisos, impuestos, comisiones y el tiempo de la obra.',
        'body': '''
<h2>¿Qué es el ARV?</h2>
<p>El ARV (After Repair Value) es el precio al que podrás vender la casa ya remodelada. Se calcula con ventas recientes de casas remodeladas parecidas en el mismo barrio, no con el precio de la casa más cara de la ciudad. Si el ARV está mal calculado, todo el negocio está mal calculado.</p>

<h2>¿Cómo se aplica la regla del 70%?</h2>
<p><strong>Precio máximo de compra = ARV × 0.70 − costo de reparaciones</strong></p>
<p>El 30% restante cubre la compra y la venta, el financiamiento, los imprevistos y tu ganancia. En mercados caros como el Bay Area, algunos inversionistas usan 75%, pero eso deja menos margen de error.</p>

<h2>Ejemplo completo en Oakland</h2>
<table>
<thead><tr><th>Concepto</th><th>Monto (ejemplo)</th></tr></thead>
<tbody>
<tr><td>ARV (valor después de remodelar)</td><td>$900,000</td></tr>
<tr><td>Precio de compra (regla del 70%)</td><td>$510,000</td></tr>
<tr><td>Costos de compra (≈2%)</td><td>$10,200</td></tr>
<tr><td>Remodelación</td><td>$120,000</td></tr>
<tr><td>Imprevistos (10% de la obra)</td><td>$12,000</td></tr>
<tr><td>Costos de mantener 6 meses (intereses, impuestos, seguro, servicios)</td><td>$35,000</td></tr>
<tr><td>Costos de venta (≈6%)</td><td>$54,000</td></tr>
<tr><td><strong>Ganancia antes de impuestos</strong></td><td><strong>$158,800</strong></td></tr>
</tbody>
</table>
<p>Si la obra tarda el doble o el ARV baja 5%, la ganancia cambia mucho. Por eso conviene correr el número con escenarios pesimistas antes de ofertar.</p>

<h2>¿Qué costos se olvidan con más frecuencia?</h2>
<ul>
<li><strong>Permisos y planos:</strong> en ciudades como <a href="/areas/oakland/">Oakland</a> los permisos pueden tardar semanas y cambiar el calendario.</li>
<li><strong>Cimientos y estructura:</strong> muchas casas antiguas necesitan refuerzo sísmico.</li>
<li><strong>Drenaje (sewer lateral):</strong> en ciudades servidas por EBMUD, al vender necesitas el certificado de la tubería privada.</li>
<li><strong>Pintura con plomo:</strong> en casas de antes de 1978, el contratista debe estar certificado por la EPA para trabajar con plomo.</li>
<li><strong>Tiempo:</strong> cada mes extra suma intereses, impuestos y seguro.</li>
</ul>

<h2>¿Cómo se financia un flip?</h2>
<ul>
<li><strong>Efectivo:</strong> el más rápido y el que te da más fuerza al negociar.</li>
<li><strong>Préstamos "hard money" o privados:</strong> a corto plazo, aprobados según el valor de la propiedad, con tasas y puntos más altos que un préstamo normal. Suelen financiar parte de la compra y de la obra.</li>
<li><strong>Socios:</strong> uno pone el capital y otro la experiencia; deja todo por escrito.</li>
</ul>

<h2>¿Cuánto pagas de impuestos en un flip?</h2>
<p>Si vendes en menos de un año, la ganancia se considera de corto plazo y se grava como ingreso normal. Si haces flips seguido, el IRS puede tratarte como negocio. California grava todas las ganancias como ingreso normal. Habla con un contador antes de comprar.</p>

<h2>¿Dónde buscar oportunidades?</h2>
<p>En el Bay Area, las casas antiguas que necesitan trabajo están sobre todo en barrios de <a href="/areas/oakland/">Oakland</a>, <a href="/areas/richmond/">Richmond</a> y <a href="/areas/antioch/">Antioch</a>. Tres de mis ventas más recientes en Oakland fueron proyectos Fix & Flip; puedes verlas en el <a href="/#portafolio">portafolio</a>.</p>
''',
        'faq': [
            ('¿Cuánto dinero necesito para empezar un Fix & Flip?',
             'Depende del financiamiento. Aun con un préstamo hard money, normalmente debes poner una parte de la compra, los costos de cierre, parte de la obra y una reserva para imprevistos.'),
            ('¿La regla del 70% funciona en el Bay Area?',
             'Sirve como filtro rápido. Con los precios del Bay Area es difícil encontrar casas al 70%, y algunos inversionistas aceptan 75%, pero solo si los números completos siguen dejando ganancia en un escenario pesimista.'),
            ('¿Cuánto tarda un flip?',
             'Varios meses entre la compra, los permisos, la obra y la venta. Los retrasos en permisos y contratistas son el riesgo más común.'),
        ],
        'sources': [
            ('EPA: programa de renovación, reparación y pintura (plomo)', 'https://www.epa.gov/lead/renovation-repair-and-painting-program'),
            ('EBMUD: tuberías de drenaje privadas (sewer lateral)', 'https://www.ebmud.com/wastewater/private-sewer-laterals'),
            ('IRS: Tema 409, ganancias y pérdidas de capital', 'https://www.irs.gov/taxtopics/tc409'),
        ],
    },
    {
        'slug': 'casas-mas-baratas-bay-area-east-bay',
        'category': 'Mercado',
        'title': '¿Dónde comprar casa más barata en el Bay Area? 7 ciudades del East Bay más accesibles (2026)',
        'seo_title': 'Casas más baratas en el Bay Area: 7 ciudades del East Bay (2026)',
        'desc': 'Las ciudades más accesibles del East Bay en 2026: Pittsburg, Antioch, Richmond, Brentwood, Concord, Oakland y Hayward. Precios medianos, BART y para quién conviene cada una.',
        'keywords': ['casas baratas Bay Area', 'dónde comprar casa East Bay', 'ciudades accesibles Bay Area 2026', 'casas en venta Antioch Pittsburg'],
        'cities': ['pittsburg', 'antioch', 'richmond', 'brentwood', 'concord', 'oakland', 'hayward'],
        'related': ['cuanto-enganche-para-comprar-casa-california', 'programas-primera-casa-california', 'comprar-casa-con-itin-california'],
        'answer': 'En 2026, las ciudades más accesibles cerca del centro del Bay Area están en el este de Contra Costa: Pittsburg y Antioch tienen precios medianos de alrededor de $590,000, seguidas por Richmond (alrededor de $650,000). Brentwood, Concord y Oakland rondan entre $745,000 y $775,000, según Redfin. Todas tienen BART o una estación cercana.',
        'body': '''
<h2>¿Cuáles son las ciudades más accesibles en 2026?</h2>
<table>
<thead><tr><th>Ciudad</th><th>Precio mediano aproximado</th><th>Dato de Redfin</th><th>BART</th></tr></thead>
<tbody>
<tr><td><a href="/areas/pittsburg/">Pittsburg</a></td><td>$590,000</td><td>septiembre de 2026</td><td>Pittsburg/Bay Point y Pittsburg Center</td></tr>
<tr><td><a href="/areas/antioch/">Antioch</a></td><td>$592,000</td><td>julio a septiembre de 2026</td><td>Antioch</td></tr>
<tr><td><a href="/areas/richmond/">Richmond</a></td><td>$650,000</td><td>mayo de 2026</td><td>Richmond, más ferry a SF</td></tr>
<tr><td><a href="/areas/brentwood/">Brentwood</a></td><td>$746,000</td><td>junio de 2026</td><td>Antioch (autobús express)</td></tr>
<tr><td><a href="/areas/concord/">Concord</a></td><td>$758,000</td><td>junio a agosto de 2026</td><td>Concord y North Concord/Martinez</td></tr>
<tr><td><a href="/areas/oakland/">Oakland</a></td><td>$773,000</td><td>julio a septiembre de 2026</td><td>8 estaciones</td></tr>
<tr><td><a href="/areas/hayward/">Hayward</a></td><td>$849,000</td><td>junio a agosto de 2026</td><td>Hayward y South Hayward</td></tr>
</tbody>
</table>
<p>La mediana incluye casas y condominios, y cada ciudad tiene barrios mucho más caros y más baratos que el promedio.</p>

<h3>Pittsburg</h3>
<p>Dos estaciones de BART y una comunidad latina grande. Buena opción para primeros compradores que trabajan en Concord, Walnut Creek u Oakland. <a href="/areas/pittsburg/">Ver Pittsburg</a>.</p>

<h3>Antioch</h3>
<p>Casas y terrenos más grandes por el mismo presupuesto, con BART desde 2018. Ideal si buscas espacio para la familia. <a href="/areas/antioch/">Ver Antioch</a>.</p>

<h3>Richmond</h3>
<p>Cerca de Berkeley y con ferry a San Francisco. Los precios cambian mucho de un barrio a otro, desde Marina Bay hasta Hilltop. <a href="/areas/richmond/">Ver Richmond</a>.</p>

<h3>Brentwood</h3>
<p>Casas más nuevas, ambiente de pueblo y comunidades para mayores de 55. No tiene BART propio, pero hay autobús express al BART de Antioch. <a href="/areas/brentwood/">Ver Brentwood</a>.</p>

<h3>Concord</h3>
<p>La ciudad más grande de Contra Costa, con ubicación central sobre la I-680 y la autopista 4. Hay condominios accesibles y casas en Clayton e Ygnacio Valley. <a href="/areas/concord/">Ver Concord</a>.</p>

<h3>Oakland</h3>
<p>La más variada: desde condominios hasta casas en las colinas, y casas antiguas con potencial de remodelación en East Oakland. <a href="/areas/oakland/">Ver Oakland</a>.</p>

<h3>Hayward</h3>
<p>Ubicación central entre Oakland, la Península y el sur de la bahía. Revisa el riesgo sísmico de la falla de Hayward antes de comprar. <a href="/areas/hayward/">Ver Hayward</a>.</p>

<h2>¿Cómo eliges entre una ciudad y otra?</h2>
<ul>
<li><strong>Tu ruta al trabajo:</strong> prueba el trayecto en BART o en carro a la hora pico antes de decidir.</li>
<li><strong>Pago mensual total:</strong> no solo el precio; también impuestos, seguro y HOA.</li>
<li><strong>Escuelas:</strong> el distrito depende de la dirección exacta.</li>
<li><strong>Planes a futuro:</strong> si piensas rentar la casa después, revisa la demanda de renta en la zona.</li>
</ul>
''',
        'faq': [
            ('¿Cuál es la ciudad más barata del Bay Area para comprar casa en 2026?',
             'Entre las ciudades con BART cerca del centro del Bay Area, Pittsburg y Antioch tienen los precios medianos más bajos en 2026, alrededor de $590,000 según Redfin.'),
            ('¿Conviene comprar lejos y viajar al trabajo?',
             'Depende de tu trabajo y tu familia. Comprar más lejos te da más espacio por tu dinero, pero suma tiempo y costo de traslado. Calcula los dos antes de decidir.'),
            ('¿Puedo usar programas de ayuda en estas ciudades?',
             'Sí. Los programas de CalHFA aplican en todo California; los límites de ingreso y de precio cambian por condado.'),
        ],
        'sources': [
            ('Redfin: mercado de vivienda de Pittsburg', 'https://www.redfin.com/city/14890/CA/Pittsburg/housing-market'),
            ('Redfin: mercado de vivienda de Antioch', 'https://www.redfin.com/city/588/CA/Antioch/housing-market'),
            ('Redfin: mercado de vivienda de Richmond', 'https://www.redfin.com/city/15629/CA/Richmond/housing-market'),
            ('Redfin: mercado de vivienda de Brentwood', 'https://www.redfin.com/city/2112/CA/Brentwood/housing-market'),
            ('Redfin: mercado de vivienda de Concord', 'https://www.redfin.com/city/4150/CA/Concord/housing-market'),
            ('Redfin: mercado de vivienda de Hayward', 'https://www.redfin.com/city/8439/CA/Hayward/housing-market'),
        ],
    },
    {
        'slug': 'que-hace-un-realtor-cuanto-cobra-california',
        'category': 'Guías',
        'title': '¿Qué hace un realtor y cuánto cobra en California? Lo que cambió desde 2024',
        'seo_title': '¿Qué hace un realtor y cuánto cobra en California? (2026)',
        'desc': 'Qué hace un realtor al comprar o vender, cómo funcionan las comisiones en California después de 2024, el acuerdo por escrito con el comprador (AB 2992) y cómo verificar una licencia.',
        'keywords': ['qué hace un realtor', 'cuánto cobra un realtor', 'comisión agente inmobiliario California', 'realtor que hable español'],
        'cities': ['oakland', 'san-francisco', 'concord'],
        'related': ['cuanto-cuesta-vender-casa-california', 'como-vender-tu-casa-bay-area', 'comprar-casa-con-itin-california'],
        'answer': 'Un realtor te representa al comprar o vender: te ayuda a fijar el precio o a ofertar, negocia, coordina inspecciones y escrow, y protege tus intereses en el contrato. En California las comisiones no son fijas: se negocian. Desde agosto de 2024 los compradores firman un acuerdo por escrito con su agente, y desde 2025 la ley estatal (AB 2992) exige que ese acuerdo diga cuánto se paga, qué servicios incluye y que no dure más de 3 meses.',
        'body': '''
<h2>¿Qué hace un realtor cuando compras?</h2>
<ul>
<li>Te ayuda a definir zona y presupuesto, y te conecta con prestamistas.</li>
<li>Busca casas, incluidas las que aún no están en los portales, y te acompaña a verlas.</li>
<li>Analiza el precio con ventas comparables y prepara tu oferta.</li>
<li>Negocia precio, créditos y reparaciones.</li>
<li>Coordina inspecciones, tasación, escrow y fechas límite hasta el cierre.</li>
</ul>

<h2>¿Qué hace un realtor cuando vendes?</h2>
<ul>
<li>Prepara un análisis comparativo de mercado para fijar el precio.</li>
<li>Te dice qué arreglar y qué no, y coordina fotos, staging y publicación en el MLS.</li>
<li>Organiza visitas y open houses.</li>
<li>Compara ofertas y negocia contingencias, créditos y fechas.</li>
<li>Prepara las divulgaciones y da seguimiento al escrow hasta el cierre.</li>
</ul>

<h2>¿Cuánto cobra un realtor en California?</h2>
<p>No hay una comisión fija ni una tarifa "estándar": todo se negocia. La comisión puede ser un porcentaje del precio, una cantidad fija u otra forma acordada por escrito. Al vender, tú decides si ofreces pagar parte de la comisión del agente del comprador; al comprar, tu acuerdo dice cuánto recibirá tu agente y quién lo paga (puede pagarlo el vendedor si así se negocia).</p>

<h2>¿Qué cambió en 2024 y 2025?</h2>
<table>
<thead><tr><th>Cambio</th><th>Desde</th><th>Qué significa para ti</th></tr></thead>
<tbody>
<tr><td>Las ofertas de compensación salen del MLS</td><td>Agosto de 2024</td><td>Las comisiones del agente del comprador se negocian fuera del MLS</td></tr>
<tr><td>Acuerdo por escrito con el comprador</td><td>Agosto de 2024</td><td>Firmas un acuerdo con tu agente antes de ver casas con él</td></tr>
<tr><td>Ley AB 2992 de California</td><td>1 de enero de 2025</td><td>El acuerdo debe decir la compensación, los servicios, cuándo se paga y cómo se termina, y no puede durar más de 3 meses</td></tr>
</tbody>
</table>

<h2>¿Qué preguntar antes de firmar con un agente?</h2>
<ul>
<li>¿Cuánto cobras y qué servicios incluye?</li>
<li>¿Cuánto dura el acuerdo y cómo se cancela?</li>
<li>¿Cuántas casas has vendido o comprado en esta zona?</li>
<li>¿Quién me atiende día a día: tú o tu equipo?</li>
<li>¿Puedes explicarme todo el proceso en español?</li>
</ul>

<h2>¿Cómo verificas la licencia de un agente?</h2>
<p>Busca su nombre o número de licencia en la herramienta de búsqueda pública del Department of Real Estate (DRE) de California. Ahí ves si la licencia está activa y con qué broker trabaja. "Realtor®" significa además que el agente es miembro de la National Association of Realtors y sigue su código de ética.</p>

<h2>¿Por qué ayuda tener un agente que hable español?</h2>
<p>Los contratos, divulgaciones y documentos del préstamo están en inglés. Un agente bilingüe te explica cada cláusula y cada fecha límite en tu idioma, y negocia por ti en inglés con la otra parte. Así decides con toda la información.</p>
''',
        'faq': [
            ('¿Puedo comprar una casa sin agente?',
             'Sí. Puedes negociar directamente con el agente del vendedor, pero ese agente representa al vendedor. Sin agente propio, tú te encargas de revisar el precio, las divulgaciones, las inspecciones y las fechas del contrato.'),
            ('¿Quién le paga al agente del comprador?',
             'Lo define el acuerdo que firmas con tu agente. Puede pagarlo el comprador, el vendedor (si lo ofrece o se negocia en la oferta) o una combinación.'),
            ('¿El acuerdo con mi agente me obliga por mucho tiempo?',
             'No. En California, por la ley AB 2992, el acuerdo de un comprador individual no puede durar más de 3 meses y debe explicar cómo se termina.'),
        ],
        'sources': [
            ('California DRE: cambios en la representación de compradores', 'https://www.dre.ca.gov/Consumers/ConsumerAlert_20241114_Changes_to_Real_Estate_Representation.html'),
            ('California DRE: búsqueda pública de licencias', 'https://www2.dre.ca.gov/PublicASP/pplinfo.asp'),
            ('NAR: datos sobre el acuerdo de comisiones', 'https://www.nar.realtor/the-facts'),
        ],
    },
]

# Home page "Guías" section, in this order.
FEATURED = ['comprar-casa-con-itin-california', 'programas-primera-casa-california', 'cuanto-vale-mi-casa-bay-area']
