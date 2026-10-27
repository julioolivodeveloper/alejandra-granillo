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
        'related': ['preaprobacion-hipotecaria', 'cuanto-enganche-para-comprar-casa-california', 'puntaje-de-credito-para-comprar-casa'],
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
        'related': ['cuanto-ganar-para-comprar-casa-bay-area', 'programas-primera-casa-california', 'costos-de-cierre-comprador-california'],
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
        'category': 'Costos',
        'title': 'Costos de cierre al comprar casa en California (2026): cuánto son y qué incluyen',
        'seo_title': 'Costos de cierre al comprar casa en California (2026)',
        'desc': 'Los costos de cierre para el comprador en California suelen ser de 2% a 5% del precio. Qué incluyen, quién paga qué, el impuesto de transferencia y cómo reducirlos.',
        'keywords': ['costos de cierre California', 'closing costs comprador', 'escrow California', 'impuesto de transferencia'],
        'cities': ['oakland', 'san-leandro', 'walnut-creek'],
        'related': ['impuesto-a-la-propiedad-california', 'seguro-de-casa-california', 'cuanto-enganche-para-comprar-casa-california'],
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
        'related': ['adu-california', 'cuanto-vale-mi-casa-bay-area', 'inspeccion-de-casa-california'],
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
        'related': ['cuanto-ganar-para-comprar-casa-bay-area', 'rentar-o-comprar-casa-bay-area', 'programas-primera-casa-california'],
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
    {
        'slug': 'pasos-para-comprar-casa-california',
        'category': 'Comprar',
        'title': 'Pasos para comprar casa en California (2026): guía completa de principio a fin',
        'seo_title': 'Pasos para comprar casa en California (2026)',
        'desc': 'Los 10 pasos para comprar casa en California en 2026: presupuesto, preaprobación, agente, oferta, depósito, contingencias, inspección, tasación, escrow y cierre, con el tiempo de cada etapa.',
        'keywords': ['pasos para comprar casa', 'proceso de compra de casa California', 'cómo comprar una casa', 'escrow California'],
        'cities': ['oakland', 'concord', 'antioch'],
        'related': ['preaprobacion-hipotecaria', 'inspeccion-de-casa-california', 'cuanto-enganche-para-comprar-casa-california'],
        'answer': 'Para comprar casa en California: define tu presupuesto, consigue una preaprobación, firma con un agente, haz tu oferta y, cuando la acepten, deposita el dinero de buena fe en escrow (normalmente dentro de 3 días hábiles). Luego tienes un periodo de contingencias para inspección, tasación y préstamo, que en el contrato estándar suele ser de 17 días. Desde que aceptan tu oferta, el cierre suele tardar de 30 a 45 días.',
        'body': '''
<h2>¿Cuáles son los pasos y cuánto tarda cada uno?</h2>
<table>
<thead><tr><th>Paso</th><th>Qué haces</th><th>Tiempo aproximado</th></tr></thead>
<tbody>
<tr><td>1. Presupuesto</td><td>Calculas cuánto puedes pagar al mes y cuánto tienes ahorrado</td><td>1 a 2 semanas</td></tr>
<tr><td>2. Preaprobación</td><td>El prestamista revisa tus documentos y te da una carta</td><td>Unos días</td></tr>
<tr><td>3. Agente</td><td>Firmas un acuerdo por escrito con tu agente</td><td>1 día</td></tr>
<tr><td>4. Búsqueda</td><td>Visitas casas y comparas barrios</td><td>Semanas o meses</td></tr>
<tr><td>5. Oferta</td><td>Precio, depósito, contingencias y fecha de cierre</td><td>1 a 3 días</td></tr>
<tr><td>6. Depósito</td><td>Envías el dinero de buena fe a escrow</td><td>Normalmente 3 días hábiles</td></tr>
<tr><td>7. Inspecciones</td><td>General, termitas y las que hagan falta</td><td>Primera semana</td></tr>
<tr><td>8. Tasación y préstamo</td><td>El banco valúa la casa y aprueba el préstamo</td><td>2 a 4 semanas</td></tr>
<tr><td>9. Quitar contingencias</td><td>Confirmas por escrito que sigues adelante</td><td>Normalmente día 17</td></tr>
<tr><td>10. Firma y cierre</td><td>Firmas, se registra la escritura y recibes las llaves</td><td>Día 30 a 45</td></tr>
</tbody>
</table>

<h2>¿Cómo defines tu presupuesto?</h2>
<p>Suma lo que tienes para el enganche, los costos de cierre (2% a 5% del precio) y una reserva. Después calcula un pago mensual que te deje vivir tranquilo, incluidos impuestos, seguro y HOA. Lee <a href="/blog/cuanto-ganar-para-comprar-casa-bay-area/">cuánto tienes que ganar para comprar en el Bay Area</a>.</p>

<h2>¿Por qué necesitas la preaprobación antes de buscar?</h2>
<p>En el Bay Area los vendedores casi nunca aceptan una oferta sin carta de preaprobación. Además te dice tu precio máximo real, para no enamorarte de casas que no puedes comprar. Ve <a href="/blog/preaprobacion-hipotecaria/">qué documentos piden para la preaprobación</a>.</p>

<h2>¿Qué tiene que firmar el comprador con su agente?</h2>
<p>Desde 2025, la ley de California (AB 2992) exige un acuerdo por escrito con tu agente que diga cuánto se le paga, qué servicios incluye y cuándo termina, con un máximo de 3 meses. Más detalles en <a href="/blog/que-hace-un-realtor-cuanto-cobra-california/">qué hace un realtor y cuánto cobra</a>.</p>

<h2>¿Qué incluye una oferta?</h2>
<ul>
<li><strong>Precio</strong> y tipo de préstamo.</li>
<li><strong>Depósito de buena fe</strong> (earnest money), que se abona a tu enganche al cerrar.</li>
<li><strong>Contingencias:</strong> inspección, tasación y préstamo. Te permiten salirte sin perder el depósito si algo falla dentro del plazo.</li>
<li><strong>Fecha de cierre</strong> y, si aplica, créditos que pides al vendedor.</li>
</ul>

<h2>¿Qué pasa durante el escrow?</h2>
<p>Escrow es una compañía neutral que guarda el dinero y los documentos. Durante esas semanas haces tus inspecciones, revisas las divulgaciones del vendedor, el banco hace la tasación y aprueba el préstamo, y contratas el seguro de la casa. Antes de que venza cada contingencia decides si sigues, negocias o te sales.</p>

<h2>¿Qué pasa si la tasación sale baja?</h2>
<p>Si el tasador del banco valúa la casa por debajo del precio, el banco presta según el valor más bajo. Puedes pagar la diferencia, negociar una rebaja con el vendedor, dividir la diferencia o, si tu contingencia de tasación sigue vigente, cancelar.</p>

<h2>¿Cómo es el día del cierre?</h2>
<p>Al menos tres días hábiles antes recibes el Closing Disclosure con los montos finales. Firmas ante notario, envías el resto del dinero por transferencia y, cuando el condado registra la escritura, la casa es tuya. Ve la guía de <a href="/blog/costos-de-cierre-comprador-california/">costos de cierre</a>.</p>

<h2>¿Qué errores debes evitar?</h2>
<ul>
<li>Buscar casa antes de tener la preaprobación.</li>
<li>Saltarte la inspección para "ganar" la oferta sin saber lo que compras.</li>
<li>Abrir tarjetas, comprar carro o cambiar de trabajo antes de cerrar.</li>
<li>Dejar pasar las fechas de las contingencias sin decidir por escrito.</li>
</ul>
''',
        'faq': [
            ('¿Cuánto tarda comprar una casa en California?',
             'La búsqueda depende de ti y del mercado. Desde que el vendedor acepta tu oferta, el cierre suele tardar de 30 a 45 días con préstamo, o menos si pagas en efectivo.'),
            ('¿Puedo retirarme después de que aceptan mi oferta?',
             'Sí, dentro de tus contingencias y siguiendo los pasos del contrato, y normalmente recuperas tu depósito. Si te retiras sin una contingencia vigente, podrías perderlo.'),
            ('¿Cuánto se deposita al hacer una oferta?',
             'Se negocia en cada oferta. En California es común un depósito de alrededor de 3% del precio, que se abona al enganche al cerrar.'),
        ],
        'sources': [
            ('CFPB: guía para comprar casa', 'https://www.consumerfinance.gov/owning-a-home/'),
            ('CFPB: el Closing Disclosure', 'https://www.consumerfinance.gov/owning-a-home/closing-disclosure/'),
            ('California DRE: cambios en la representación de compradores', 'https://www.dre.ca.gov/Consumers/ConsumerAlert_20241114_Changes_to_Real_Estate_Representation.html'),
        ],
    },
    {
        'slug': 'preaprobacion-hipotecaria',
        'category': 'Comprar',
        'title': 'Preaprobación hipotecaria: qué es, qué documentos piden y cuánto dura (2026)',
        'seo_title': 'Preaprobación hipotecaria: qué es y qué documentos piden',
        'desc': 'Qué es la preaprobación para un préstamo de casa, en qué se diferencia de la precalificación, qué documentos piden (también si trabajas por tu cuenta), si afecta tu crédito y cuánto dura.',
        'keywords': ['preaprobación hipotecaria', 'preaprobación para comprar casa', 'documentos para préstamo de casa', 'precalificación vs preaprobación'],
        'cities': ['hayward', 'san-leandro', 'pittsburg'],
        'related': ['pasos-para-comprar-casa-california', 'puntaje-de-credito-para-comprar-casa', 'cuanto-ganar-para-comprar-casa-bay-area'],
        'answer': 'La preaprobación es una carta del prestamista que dice cuánto te puede prestar después de revisar tu crédito, ingresos, deudas y ahorros con documentos. No es lo mismo que la precalificación, que es un estimado con lo que tú le dices. En el Bay Area casi ningún vendedor acepta una oferta sin preaprobación, y normalmente es válida de 60 a 90 días.',
        'body': '''
<h2>¿Qué diferencia hay entre precalificación y preaprobación?</h2>
<table>
<thead><tr><th></th><th>Precalificación</th><th>Preaprobación</th></tr></thead>
<tbody>
<tr><td>Información</td><td>Lo que tú declaras</td><td>Documentos verificados y reporte de crédito</td></tr>
<tr><td>Tiempo</td><td>Minutos</td><td>Unos días</td></tr>
<tr><td>Peso en una oferta</td><td>Bajo</td><td>Alto: el vendedor sabe que puedes conseguir el préstamo</td></tr>
</tbody>
</table>

<h2>¿Qué documentos piden?</h2>
<p><strong>Si eres asalariado (W-2):</strong></p>
<ul>
<li>Talones de pago de los últimos 30 días.</li>
<li>Formas W-2 de los últimos dos años.</li>
<li>Estados de cuenta de banco de los últimos dos meses, todas las páginas.</li>
<li>Identificación con foto y autorización para revisar tu crédito.</li>
</ul>
<p><strong>Si trabajas por tu cuenta o recibes 1099:</strong> las declaraciones de impuestos completas de los últimos dos años y, a veces, un estado de pérdidas y ganancias del año. Si compras con ITIN, mira los requisitos en <a href="/blog/comprar-casa-con-itin-california/">comprar casa con ITIN</a>.</p>

<h2>¿La preaprobación baja tu crédito?</h2>
<p>El prestamista hace una consulta "dura" a tu crédito, que puede bajar tu puntaje unos pocos puntos por un tiempo. Si comparas varios prestamistas en un periodo corto, los modelos de puntaje cuentan esas consultas de préstamo hipotecario como una sola. Por eso conviene comparar en la misma semana o dos. Más en <a href="/blog/puntaje-de-credito-para-comprar-casa/">qué crédito necesitas para comprar casa</a>.</p>

<h2>¿Cuánto dura la carta?</h2>
<p>Normalmente de 60 a 90 días, según el prestamista. Si se vence o cambia tu situación, el prestamista actualiza tus documentos y te da una carta nueva.</p>

<h2>¿Qué no debes hacer después de la preaprobación?</h2>
<ul>
<li>Cambiar de trabajo o pasar de asalariado a independiente.</li>
<li>Abrir tarjetas, financiar muebles o comprar carro.</li>
<li>Depositar dinero que no puedas documentar.</li>
<li>Atrasarte en cualquier pago.</li>
</ul>

<h2>¿La preaprobación garantiza el préstamo?</h2>
<p>No. Después de aceptar tu oferta, el banco hace la aprobación final (underwriting): vuelve a revisar documentos, tasa la casa y confirma que nada cambió. La preaprobación reduce mucho el riesgo, pero no lo elimina.</p>

<h2>¿Cómo comparas prestamistas?</h2>
<p>Pide un Loan Estimate a dos o tres prestamistas el mismo día y compara la tasa, los puntos, los cargos del préstamo y el pago mensual total. Una carta de un prestamista local que responde rápido también ayuda a que el agente del vendedor confíe en tu oferta.</p>
''',
        'faq': [
            ('¿Cuánto cuesta una preaprobación?',
             'Muchos prestamistas no cobran por la preaprobación. Algunos cobran el reporte de crédito; pregunta antes de autorizarlo.'),
            ('¿Puedo tener preaprobaciones de dos prestamistas?',
             'Sí. Es una buena forma de comparar. Si las haces en un periodo corto, el impacto en tu crédito es mínimo.'),
            ('¿Me pueden negar el préstamo después de preaprobarme?',
             'Puede pasar si cambian tus ingresos, tus deudas o tu crédito, si la tasación sale baja o si aparece algo en los documentos. Por eso no debes hacer cambios financieros grandes hasta cerrar.'),
        ],
        'sources': [
            ('CFPB: diferencia entre precalificación y preaprobación', 'https://www.consumerfinance.gov/ask-cfpb/whats-the-difference-between-a-prequalification-letter-and-a-preapproval-letter-en-127/'),
            ('CFPB: cómo leer tu Loan Estimate', 'https://www.consumerfinance.gov/owning-a-home/loan-estimate/'),
            ('CFPB: guía para comprar casa', 'https://www.consumerfinance.gov/owning-a-home/'),
        ],
    },
    {
        'slug': 'puntaje-de-credito-para-comprar-casa',
        'category': 'Comprar',
        'title': '¿Qué puntaje de crédito necesitas para comprar casa? Requisitos y cómo subirlo (2026)',
        'seo_title': 'Puntaje de crédito para comprar casa (2026) y cómo subirlo',
        'desc': 'Qué crédito necesitas para comprar casa en 2026: FHA desde 580, préstamos convencionales sin mínimo fijo de Fannie Mae desde noviembre de 2025, VA e ITIN. Y cómo subir tu puntaje antes de comprar.',
        'keywords': ['puntaje de crédito para comprar casa', 'crédito mínimo FHA', 'cómo subir mi crédito', 'credit score para casa'],
        'cities': ['antioch', 'pittsburg', 'richmond'],
        'related': ['preaprobacion-hipotecaria', 'cuanto-enganche-para-comprar-casa-california', 'comprar-casa-con-itin-california'],
        'answer': 'Con FHA puedes comprar con un puntaje de 580 y 3.5% de enganche, o de 500 a 579 con 10%. Desde noviembre de 2025 Fannie Mae ya no exige un mínimo fijo de 620 en los préstamos convencionales que evalúa con su sistema automático, aunque muchos prestamistas siguen pidiendo alrededor de 620. Un puntaje más alto te da mejor tasa, así que subirlo antes de comprar puede ahorrarte miles de dólares.',
        'body': '''
<h2>¿Qué puntaje pide cada tipo de préstamo?</h2>
<table>
<thead><tr><th>Préstamo</th><th>Puntaje que suelen pedir</th></tr></thead>
<tbody>
<tr><td>FHA</td><td>580 con 3.5% de enganche; 500 a 579 con 10%</td></tr>
<tr><td>Convencional</td><td>Fannie Mae quitó el mínimo fijo de 620 en noviembre de 2025; muchos prestamistas todavía piden alrededor de 620</td></tr>
<tr><td>VA</td><td>El VA no fija un mínimo; cada prestamista pone el suyo</td></tr>
<tr><td>ITIN</td><td>Muchos piden alrededor de 660 o crédito alternativo</td></tr>
<tr><td>Jumbo</td><td>Suelen pedir puntajes más altos</td></tr>
</tbody>
</table>
<p>Aunque califiques con un puntaje bajo, la tasa y el seguro hipotecario serán más caros. Pasar de un rango de puntaje al siguiente puede bajar tu pago mensual.</p>

<h2>¿Qué forma tu puntaje?</h2>
<ul>
<li><strong>Historial de pagos (35%):</strong> pagar todo a tiempo es lo más importante.</li>
<li><strong>Cuánto debes (30%):</strong> sobre todo, qué porcentaje del límite de tus tarjetas usas.</li>
<li><strong>Antigüedad (15%):</strong> cuánto tiempo tienen tus cuentas.</li>
<li><strong>Crédito nuevo (10%)</strong> y <strong>tipos de crédito (10%)</strong>.</li>
</ul>

<h2>¿Cómo subes tu puntaje antes de comprar?</h2>
<ol>
<li><strong>Revisa tus reportes gratis</strong> en AnnualCreditReport.com y disputa los errores.</li>
<li><strong>Baja el saldo de tus tarjetas</strong> por debajo de 30% del límite, y mejor aún de 10%.</li>
<li><strong>Paga antes de la fecha de corte</strong> para que el reporte muestre un saldo bajo.</li>
<li><strong>No cierres tarjetas viejas</strong>: bajan tu antigüedad y tu crédito disponible.</li>
<li><strong>No abras crédito nuevo</strong> en los meses antes de comprar.</li>
<li><strong>Pon tus pagos en automático</strong> para no atrasarte nunca.</li>
<li><strong>Si no tienes historial:</strong> una tarjeta asegurada o un préstamo para construir crédito, y reportar tu renta.</li>
<li><strong>Pide a tu prestamista un "rapid rescore"</strong> si pagaste una deuda y necesitas que se refleje rápido.</li>
</ol>

<h2>¿Qué pasa con las cuentas en cobranza?</h2>
<p>Depende del préstamo y del monto. Algunas cobranzas pequeñas no impiden el préstamo, pero las deudas con el gobierno o los juicios pendientes suelen tener que resolverse antes. Habla con tu prestamista antes de pagar o negociar una cuenta vieja, porque el orden importa.</p>

<h2>¿Sirven las compañías de "reparación de crédito"?</h2>
<p>Nadie puede borrar información negativa que sea correcta. Lo que una compañía hace, disputar errores, lo puedes hacer tú gratis. Desconfía de quien cobra por adelantado o promete borrar todo.</p>
''',
        'faq': [
            ('¿Cuánto tarda en subir mi puntaje?',
             'Bajar el saldo de tus tarjetas puede reflejarse en uno o dos ciclos de facturación. Los atrasos pesan menos con el tiempo, pero tardan años en desaparecer del reporte.'),
            ('¿Revisar mi propio crédito lo baja?',
             'No. Revisar tu propio crédito es una consulta "suave" y no afecta tu puntaje. Solo las solicitudes de crédito nuevo hacen consultas "duras".'),
            ('¿Puedo comprar casa si nunca he tenido crédito?',
             'Sí, en algunos casos. Algunos préstamos aceptan crédito alternativo, como pagos de renta, luz y teléfono a tiempo, sobre todo los préstamos ITIN y algunos FHA.'),
        ],
        'sources': [
            ('HUD: préstamos FHA', 'https://www.hud.gov/buying/loans'),
            ('MPA: Fannie Mae elimina el puntaje mínimo en Desktop Underwriter', 'https://www.mpamag.com/us/mortgage-industry/industry-trends/fannie-mae-scraps-minimum-credit-score-for-du-loans/555870'),
            ('AnnualCreditReport.com: reportes de crédito gratis', 'https://www.annualcreditreport.com/'),
            ('myFICO: qué forma tu puntaje', 'https://www.myfico.com/credit-education/whats-in-your-credit-score'),
            ('CFPB: cómo disputar un error en tu reporte de crédito', 'https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/'),
        ],
    },
    {
        'slug': 'cuanto-ganar-para-comprar-casa-bay-area',
        'category': 'Comprar',
        'title': '¿Cuánto tienes que ganar para comprar casa en el Bay Area? (2026)',
        'seo_title': '¿Cuánto tienes que ganar para comprar casa en el Bay Area? (2026)',
        'desc': 'Cuánto ingreso necesitas para comprar casa en el Bay Area con la tasa de 7.32% de octubre de 2026: ejemplos con casas de $600,000, $775,000 y $900,000, y cómo calcula el banco lo que puedes pagar.',
        'keywords': ['cuánto tengo que ganar para comprar casa', 'ingreso para comprar casa Bay Area', 'cuánta casa puedo pagar', 'debt to income'],
        'cities': ['pittsburg', 'antioch', 'concord', 'oakland'],
        'related': ['cuanto-enganche-para-comprar-casa-california', 'casas-mas-baratas-bay-area-east-bay', 'rentar-o-comprar-casa-bay-area'],
        'answer': 'Con la tasa promedio de 7.32% a 30 años (Freddie Mac, 22 de octubre de 2026) y 10% de enganche, una casa de $600,000 tiene un pago total de unos $4,700 al mes, y necesitas ganar entre $131,000 y $156,000 al año si no tienes otras deudas. Para una casa de $775,000, el rango sube a $168,000 a $200,000. Los bancos revisan que tus deudas totales no pasen de alrededor de 43% a 50% de tu ingreso bruto.',
        'body': '''
<h2>¿Cómo calcula el banco cuánto puedes pagar?</h2>
<p>El prestamista usa la <strong>relación deuda-ingreso</strong> (DTI): divide todos tus pagos mensuales de deudas, incluido el nuevo pago de la casa, entre tu ingreso bruto mensual. Muchos préstamos aceptan hasta alrededor de 43%, y algunos programas llegan a 50% si tienes buen crédito o ahorros. Que el banco te apruebe no significa que ese pago te deje vivir cómodo.</p>

<h2>¿Cuánto necesitas ganar según el precio?</h2>
<table>
<thead><tr><th>Precio</th><th>Préstamo (10% de enganche)</th><th>Pago mensual total*</th><th>Ingreso anual necesario**</th></tr></thead>
<tbody>
<tr><td>$600,000</td><td>$540,000</td><td>≈ $4,700</td><td>$131,000 a $156,000</td></tr>
<tr><td>$775,000</td><td>$697,500</td><td>≈ $6,000</td><td>$168,000 a $200,000</td></tr>
<tr><td>$900,000</td><td>$810,000</td><td>≈ $6,950</td><td>$194,000 a $232,000</td></tr>
</tbody>
</table>
<p>* Capital e intereses al 7.32% a 30 años, impuesto de propiedad de 1.2% al año, seguro de $150 al mes y seguro hipotecario (PMI) estimado. No incluye HOA.<br>** El número menor supone que el banco acepta 43% de deuda y que no tienes otras deudas; el mayor es un pago más cómodo, de 36% de tu ingreso.</p>
<p>Como referencia, en 2026 el precio mediano está cerca de $590,000 en <a href="/areas/pittsburg/">Pittsburg</a> y <a href="/areas/antioch/">Antioch</a>, de $758,000 en <a href="/areas/concord/">Concord</a> y de $773,000 en <a href="/areas/oakland/">Oakland</a>, según Redfin.</p>

<h2>¿Qué cambia el número?</h2>
<ul>
<li><strong>Tus otras deudas:</strong> con un límite de 43%, un pago de carro de $600 al mes sube en unos $17,000 al año el ingreso que necesitas.</li>
<li><strong>La tasa:</strong> cada punto de tasa cambia el pago de un préstamo de $600,000 en unos $400 al mes.</li>
<li><strong>El enganche:</strong> con 20% bajas el préstamo y eliminas el PMI.</li>
<li><strong>El impuesto de tu ciudad y la HOA</strong>, si compras un condominio.</li>
</ul>

<h2>¿Cuentan los ingresos de toda la familia?</h2>
<p>Si otra persona está en el préstamo, sí: se suman sus ingresos y también sus deudas. El ingreso por cuenta propia, las propinas y las horas extra cuentan si los declaras en tus impuestos, normalmente con dos años de historial.</p>

<h2>¿Cómo puedes comprar con menos ingreso?</h2>
<ul>
<li>Buscar en <a href="/blog/casas-mas-baratas-bay-area-east-bay/">ciudades más accesibles del East Bay</a> o un condominio.</li>
<li>Usar <a href="/blog/programas-primera-casa-california/">programas de asistencia</a> para el enganche.</li>
<li>Negociar que el vendedor pague puntos para bajar tu tasa.</li>
<li>Comprar con alguien más (familia o pareja) como co-prestatario.</li>
<li>Considerar una casa con unidad adicional para rentar; lee sobre <a href="/blog/adu-california/">los ADU</a>.</li>
</ul>
''',
        'faq': [
            ('¿Qué es la relación deuda-ingreso (DTI)?',
             'Es el porcentaje de tu ingreso bruto mensual que se va en pagos de deudas, incluida la hipoteca. Si ganas $10,000 al mes y pagas $4,300 entre casa, carro y tarjetas, tu DTI es 43%.'),
            ('¿Y si las tasas bajan después de comprar?',
             'Puedes refinanciar para bajar tu pago, pero no hay garantía de que bajen. Compra con un pago que puedas sostener con la tasa de hoy.'),
            ('¿Cuenta el ingreso en efectivo que no declaro?',
             'No. Los prestamistas solo cuentan ingresos que puedas documentar, normalmente con tus declaraciones de impuestos.'),
        ],
        'sources': [
            ('Freddie Mac: encuesta semanal de tasas (PMMS)', 'https://www.freddiemac.com/pmms'),
            ('GlobeNewswire: tasas bajan a 7.32% (22 de octubre de 2026)', 'https://www.globenewswire.com/news-release/2026/10/22/3386709/0/en/mortgage-rates-decrease-to-7-32.html'),
            ('CFPB: qué es la relación deuda-ingreso', 'https://www.consumerfinance.gov/ask-cfpb/what-is-a-debt-to-income-ratio-en-1791/'),
            ('Redfin: mercado de vivienda de Oakland', 'https://www.redfin.com/city/13654/CA/Oakland/housing-market'),
        ],
    },
    {
        'slug': 'rentar-o-comprar-casa-bay-area',
        'category': 'Mercado',
        'title': '¿Rentar o comprar casa en el Bay Area? Los números reales de 2026',
        'seo_title': '¿Rentar o comprar en el Bay Area? Números de 2026',
        'desc': 'Rentar o comprar en el Bay Area en 2026: comprar la casa mediana de Oakland cuesta unos $6,100 al mes con 10% de enganche, contra $2,500 a $2,800 de renta por un departamento de 2 recámaras. Cuándo sí conviene comprar.',
        'keywords': ['rentar o comprar casa', 'conviene comprar casa 2026', 'renta vs compra Bay Area', 'renta Oakland 2026'],
        'cities': ['oakland', 'richmond', 'hayward'],
        'related': ['cuanto-ganar-para-comprar-casa-bay-area', 'casas-mas-baratas-bay-area-east-bay', 'adu-california'],
        'answer': 'En 2026, comprar en el Bay Area cuesta más al mes que rentar. Con 10% de enganche y una tasa de 7.32%, la casa mediana de Oakland (unos $773,000) sale en alrededor de $6,100 al mes, mientras que un departamento de 2 recámaras se renta por unos $2,500 a $2,800. Comprar conviene si piensas quedarte varios años, quieres un pago estable y construir patrimonio. Rentar conviene si necesitas flexibilidad o todavía no tienes reservas.',
        'body': '''
<h2>¿Cuánto cuesta al mes rentar y cuánto comprar?</h2>
<table>
<thead><tr><th>Concepto</th><th>Comprar casa de $773,000 en Oakland</th><th>Rentar 2 recámaras en Oakland</th></tr></thead>
<tbody>
<tr><td>Pago principal</td><td>$4,779 (capital e intereses, 7.32%, 10% de enganche)</td><td>$2,500 a $2,800 de renta</td></tr>
<tr><td>Impuesto de propiedad</td><td>≈ $837 (1.3% al año)</td><td>Incluido en la renta</td></tr>
<tr><td>Seguro</td><td>≈ $175</td><td>Seguro de inquilino, mucho más barato</td></tr>
<tr><td>Seguro hipotecario (PMI)</td><td>≈ $290</td><td>No aplica</td></tr>
<tr><td><strong>Total aproximado</strong></td><td><strong>≈ $6,100 al mes</strong></td><td><strong>≈ $2,500 a $2,800 al mes</strong></td></tr>
</tbody>
</table>
<p>Ojo: no es la misma vivienda. La mediana de compra incluye casas unifamiliares, y la renta es de un departamento. Un condominio de $500,000 con $450 de HOA saldría en unos $4,350 al mes con los mismos supuestos.</p>

<h2>¿Qué recuperas cuando compras?</h2>
<ul>
<li><strong>Patrimonio:</strong> en el primer año, unos $6,600 de tus pagos bajan la deuda; esa parte crece cada año.</li>
<li><strong>Plusvalía:</strong> históricamente las casas del Bay Area han subido de valor a largo plazo, aunque hay años en que bajan.</li>
<li><strong>Impuesto estable:</strong> por la Proposición 13, el valor fiscal solo sube hasta 2% al año. Ve <a href="/blog/impuesto-a-la-propiedad-california/">el impuesto a la propiedad en California</a>.</li>
<li><strong>Pago fijo:</strong> con tasa fija, tu capital e intereses no cambian en 30 años, mientras la renta suele subir.</li>
<li><strong>Deducción de intereses:</strong> solo si detallas deducciones, y sobre hasta $750,000 de deuda hipotecaria.</li>
</ul>

<h2>¿Qué costos tiene ser dueño que no tiene rentar?</h2>
<ul>
<li>Mantenimiento y reparaciones: como regla general, aparta alrededor de 1% del valor de la casa al año.</li>
<li>Costos de compra y de venta: si vendes pronto, se comen buena parte de la plusvalía.</li>
<li>Menos flexibilidad para mudarte.</li>
</ul>

<h2>¿Cuándo conviene comprar?</h2>
<ul>
<li>Piensas quedarte al menos 5 a 7 años en la zona.</li>
<li>Tienes enganche, costos de cierre y una reserva de varios meses.</li>
<li>El pago total te deja ahorrar cada mes.</li>
<li>Quieres estabilidad para tu familia o rentar parte de la casa (por ejemplo, un <a href="/blog/adu-california/">ADU</a>).</li>
</ul>

<h2>¿Cuándo conviene seguir rentando?</h2>
<ul>
<li>Podrías mudarte de ciudad o de trabajo en pocos años.</li>
<li>Comprar te dejaría sin ahorros de emergencia.</li>
<li>Tu renta está protegida: en California, la ley AB 1482 limita los aumentos en muchas viviendas a 5% más inflación, con un máximo de 10% al año, y ciudades como Oakland tienen además control de rentas en edificios más antiguos.</li>
</ul>
''',
        'faq': [
            ('¿Cuántos años tengo que quedarme para que convenga comprar?',
             'Como regla general, al menos 5 a 7 años, para que la plusvalía y lo que pagas de deuda superen los costos de comprar y vender. Depende de cuánto suban los precios y la renta.'),
            ('¿Conviene esperar a que bajen las tasas?',
             'Nadie sabe cuándo bajarán. Si encuentras la casa correcta y el pago te funciona hoy, puedes refinanciar si bajan. Si esperas, los precios también pueden subir.'),
            ('¿Un condominio es buena forma de empezar?',
             'Puede serlo: el precio de entrada es menor. Revisa la cuota de HOA, las reservas de la asociación y si hay reparaciones grandes en camino.'),
        ],
        'sources': [
            ('Freddie Mac: encuesta semanal de tasas (PMMS)', 'https://www.freddiemac.com/pmms'),
            ('Apartment List: reporte de rentas de Oakland', 'https://www.apartmentlist.com/rent-report/ca/oakland'),
            ('RentReboot: rentas en Oakland por recámaras', 'https://rentreboot.com/sf-bay/average/oakland'),
            ('Redfin: mercado de vivienda de Oakland', 'https://www.redfin.com/city/13654/CA/Oakland/housing-market'),
        ],
    },
    {
        'slug': 'impuesto-a-la-propiedad-california',
        'category': 'Costos',
        'title': 'Impuesto a la propiedad en California (2026): cuánto se paga, Prop 13 y Prop 19',
        'seo_title': 'Impuesto a la propiedad en California (2026): Prop 13 y 19',
        'desc': 'Cuánto se paga de impuesto de propiedad en California en 2026: 1% más cargos locales (entre 1.1% y 1.4% en el Bay Area), límite de 2% anual por la Prop 13, factura suplementaria, exención de $7,000 y Prop 19.',
        'keywords': ['impuesto a la propiedad California', 'property tax California', 'Prop 13', 'Prop 19', 'factura suplementaria'],
        'cities': ['oakland', 'brentwood', 'walnut-creek'],
        'related': ['costos-de-cierre-comprador-california', 'casa-heredada-california', 'seguro-de-casa-california'],
        'answer': 'En California el impuesto a la propiedad es 1% del valor fiscal de la casa más los cargos locales aprobados por los votantes, así que en el Bay Area el total suele quedar entre 1.1% y 1.4% al año. Por la Proposición 13, el valor fiscal se fija con el precio de compra y solo puede subir hasta 2% al año mientras seas dueño. Al comprar llega una factura suplementaria, y si vives en la casa puedes pedir la exención de propietario de $7,000.',
        'body': '''
<h2>¿Cómo se calcula el impuesto?</h2>
<p>Valor fiscal × tasa total de tu zona. Por ejemplo, una casa comprada en $750,000 con una tasa total de 1.25%:</p>
<table>
<thead><tr><th>Concepto</th><th>Monto</th></tr></thead>
<tbody>
<tr><td>Impuesto anual</td><td>$9,375</td></tr>
<tr><td>Equivalente mensual</td><td>≈ $781</td></tr>
<tr><td>Ahorro con la exención de propietario ($7,000 de valor)</td><td>≈ $88 al año</td></tr>
</tbody>
</table>
<p>La tasa total cambia según la ciudad y el distrito; en Oakland suele estar entre las más altas del condado de Alameda. Revisa la factura actual de la casa antes de ofertar.</p>

<h2>¿Qué dice la Proposición 13?</h2>
<ul>
<li>El valor fiscal se fija al comprar (o al construir algo nuevo).</li>
<li>Mientras seas dueño, ese valor solo puede subir hasta 2% al año, aunque el mercado suba mucho más.</li>
<li>Cuando la casa cambia de dueño, se vuelve a valorar al precio de venta.</li>
</ul>
<p>Por eso dos casas iguales en la misma calle pueden pagar impuestos muy distintos.</p>

<h2>¿Qué es la factura suplementaria?</h2>
<p>Cuando compras, el condado ajusta el valor de la casa a tu precio de compra a partir de la fecha del cierre. Unos meses después llega una o dos facturas suplementarias por la diferencia. Normalmente no las paga la cuenta de reserva del banco, así que aparta ese dinero.</p>

<h2>¿Cuándo se paga?</h2>
<ul>
<li>Primera cuota: vence el 1 de noviembre y se atrasa después del 10 de diciembre.</li>
<li>Segunda cuota: vence el 1 de febrero y se atrasa después del 10 de abril.</li>
</ul>
<p>Si pagas tarde se cobra una multa de 10%. Muchos préstamos incluyen el impuesto en tu pago mensual a través de una cuenta de reserva (impound).</p>

<h2>¿Qué cambia la Proposición 19?</h2>
<p><strong>Si tienes 55 años o más</strong> (o tienes una discapacidad grave, o perdiste tu casa por un incendio o desastre), puedes llevar tu valor fiscal a otra casa en cualquier parte de California, hasta tres veces, si compras la nueva dentro de dos años de vender la anterior. Si la nueva cuesta más, se suma la diferencia.</p>
<p><strong>Si heredas de tus padres,</strong> solo conservas su valor fiscal si haces de la casa tu residencia principal, y con un límite: para transferencias del 16 de febrero de 2025 al 15 de febrero de 2027 se excluyen hasta $1,044,586 sobre su valor fiscal. Lee <a href="/blog/casa-heredada-california/">qué hacer si heredaste una casa</a>.</p>

<h2>¿Hay otros cargos?</h2>
<p>En desarrollos más nuevos, como algunos del este de Contra Costa, puede haber impuestos especiales Mello-Roos o cargos de evaluación que se suman al impuesto normal. Aparecen en la factura y en las divulgaciones; pregúntalos antes de ofertar en una casa nueva en lugares como <a href="/areas/brentwood/">Brentwood</a>.</p>
''',
        'faq': [
            ('¿Sube mi impuesto si remodelo?',
             'Solo se vuelve a valorar la parte nueva, como un cuarto agregado o un ADU. El resto de la casa conserva su valor de la Proposición 13.'),
            ('¿Puedo pedir que bajen mi valor fiscal si los precios cayeron?',
             'Sí. Si el valor de mercado bajó del valor fiscal, puedes pedir una reducción temporal (Proposición 8) al asesor del condado o apelar.'),
            ('¿Hay ayuda para personas mayores?',
             'El programa de posposición del impuesto del Contralor de California permite a personas de 62 años o más, ciegas o con discapacidad, y con ingresos dentro del límite, posponer el pago del impuesto de su casa.'),
        ],
        'sources': [
            ('BOE: Proposición 19', 'https://www.boe.ca.gov/prop19/'),
            ('BOE: ajuste de la exclusión de la Prop 19 (2025)', 'https://boe.ca.gov/news/2025/NR-25-02.htm'),
            ('BOE: exención de propietario', 'https://www.boe.ca.gov/proptaxes/homeowners_exemption.htm'),
            ('Contralor de California: posposición del impuesto a la propiedad', 'https://www.sco.ca.gov/ardtax_prop_tax_postponement.html'),
        ],
    },
    {
        'slug': 'inspeccion-de-casa-california',
        'category': 'Comprar',
        'title': 'Inspección de casa antes de comprar en California: qué revisan, cuánto cuesta y qué negociar',
        'seo_title': 'Inspección de casa en California: qué revisan y qué negociar',
        'desc': 'Qué incluye la inspección general y la de termitas (Sección 1 y Sección 2) al comprar casa en California, otras inspecciones que conviene hacer en el Bay Area, cuánto cuestan y cómo negociar reparaciones.',
        'keywords': ['inspección de casa', 'home inspection California', 'inspección de termitas sección 1 sección 2', 'qué revisa un inspector'],
        'cities': ['oakland', 'richmond', 'san-leandro'],
        'related': ['pasos-para-comprar-casa-california', 'fix-and-flip-bay-area-regla-70', 'seguro-de-casa-california'],
        'answer': 'Antes de comprar en California normalmente se hacen dos inspecciones: la general, que revisa estructura, techo, plomería, electricidad y sistemas, y la de termitas y hongos (pest), que separa los problemas en Sección 1 (daño o infestación activa) y Sección 2 (condiciones que pueden causarlos). Se hacen durante tu contingencia de inspección, que en el contrato estándar suele ser de 17 días, y sirven para pedir reparaciones, créditos o salirte del contrato.',
        'body': '''
<h2>¿Qué revisa la inspección general?</h2>
<ul>
<li>Cimientos, estructura y señales de movimiento.</li>
<li>Techo, canaletas y drenaje del terreno.</li>
<li>Plomería, calentador de agua (con sus correas sísmicas) y fugas.</li>
<li>Panel eléctrico, cableado y enchufes.</li>
<li>Calefacción, ventilación y aire acondicionado.</li>
<li>Ventanas, puertas, ático, sótano o crawlspace, y detectores de humo y monóxido de carbono.</li>
</ul>

<h2>¿Qué son la Sección 1 y la Sección 2 en la inspección de termitas?</h2>
<table>
<thead><tr><th>Sección</th><th>Qué significa</th><th>Ejemplos</th></tr></thead>
<tbody>
<tr><td>Sección 1</td><td>Daño o infestación activa</td><td>Termitas, hongos o pudrición de madera</td></tr>
<tr><td>Sección 2</td><td>Condiciones que pueden causar daño en el futuro</td><td>Humedad, fugas, madera en contacto con la tierra</td></tr>
<tr><td>Más inspección</td><td>Áreas que no se pudieron revisar</td><td>Zonas cubiertas o sin acceso</td></tr>
</tbody>
</table>
<p>Quién paga las reparaciones se negocia. Es común que el vendedor se haga cargo de la Sección 1, y algunos préstamos piden que se reparen ciertos daños antes de cerrar.</p>

<h2>¿Qué otras inspecciones conviene hacer en el Bay Area?</h2>
<ul>
<li><strong>Tubería de drenaje (sewer lateral):</strong> una cámara revisa la tubería hasta la calle. En ciudades servidas por EBMUD, como <a href="/areas/oakland/">Oakland</a>, se necesita un certificado al vender.</li>
<li><strong>Cimientos y refuerzo sísmico:</strong> en casas antiguas, revisa si la casa está anclada a los cimientos.</li>
<li><strong>Techo y chimenea</strong>, si el inspector general lo recomienda.</li>
<li><strong>Permisos:</strong> pide el historial de permisos en la ciudad para confirmar que las ampliaciones son legales.</li>
<li><strong>Paneles solares:</strong> revisa si son propios, rentados o financiados, porque cambia el contrato.</li>
</ul>

<h2>¿Cuánto cuestan?</h2>
<p>La inspección general suele costar varios cientos de dólares y sube con el tamaño de la casa; para una casa de 1,500 a 2,500 pies cuadrados, una referencia común es de $400 a $600. El reporte de termitas puede tener un costo aparte, y las inspecciones especiales se cobran por separado. Pide cotizaciones a inspectores locales antes de que empiece tu contingencia.</p>

<h2>¿Cómo negocias lo que salga?</h2>
<ol>
<li>Separa lo importante (seguridad, estructura, agua, electricidad) de lo cosmético.</li>
<li>Pide cotizaciones de contratistas para saber el costo real.</li>
<li>Elige qué pedir: reparación, crédito al cierre o rebaja del precio. Un crédito suele ser más simple que pedir al vendedor que repare.</li>
<li>Responde antes de que venza tu contingencia, por escrito.</li>
</ol>

<h2>¿Y si el vendedor ya hizo inspecciones?</h2>
<p>En el Bay Area muchos vendedores entregan inspecciones previas. Léelas con tu agente, pero considera tu propia inspección, sobre todo si la casa es antigua o el reporte deja áreas sin revisar.</p>
''',
        'faq': [
            ('¿Puedo comprar sin hacer inspección?',
             'Sí, pero es arriesgado. Aunque renuncies a la contingencia para que tu oferta compita mejor, puedes hacer una inspección antes de ofertar para saber qué compras.'),
            ('¿El vendedor tiene que arreglar todo lo que encuentre el inspector?',
             'No. Las reparaciones se negocian. El vendedor puede aceptar, ofrecer un crédito o decir que no, y tú decides si sigues dentro de tu contingencia.'),
            ('¿Necesito inspección si la casa es nueva?',
             'Sí, se recomienda. Las casas nuevas también tienen errores de construcción, y es mejor encontrarlos antes de que termine la garantía del constructor.'),
        ],
        'sources': [
            ('Structural Pest Control Board de California', 'https://www.pestboard.ca.gov/'),
            ('EBMUD: tuberías de drenaje privadas (sewer lateral)', 'https://www.ebmud.com/wastewater/private-sewer-laterals'),
            ('Earthquake Brace + Bolt: refuerzo sísmico de casas', 'https://www.earthquakebracebolt.com/'),
        ],
    },
    {
        'slug': 'seguro-de-casa-california',
        'category': 'Costos',
        'title': 'Seguro de casa en California (2026): por qué es difícil conseguirlo y qué opciones tienes en el Bay Area',
        'seo_title': 'Seguro de casa en California (2026): FAIR Plan y opciones',
        'desc': 'Cómo conseguir seguro de casa en California en 2026: por qué las aseguradoras limitaron pólizas, qué es el FAIR Plan (subió 29.1% en promedio en octubre de 2026), el seguro contra terremotos y cómo bajar el costo.',
        'keywords': ['seguro de casa California', 'FAIR Plan California 2026', 'seguro contra incendios', 'seguro contra terremotos'],
        'cities': ['oakland', 'walnut-creek', 'hayward'],
        'related': ['costos-de-cierre-comprador-california', 'impuesto-a-la-propiedad-california', 'inspeccion-de-casa-california'],
        'answer': 'Conseguir seguro de casa en California se volvió más difícil y caro porque varias aseguradoras limitaron las pólizas nuevas por el riesgo de incendios. En la mayor parte del Bay Area todavía hay opciones del mercado normal, pero en zonas de colinas con riesgo de incendio muchas personas terminan en el California FAIR Plan, que subió sus tarifas en promedio 29.1% desde el 15 de octubre de 2026. Cotiza el seguro en cuanto te acepten la oferta: el banco lo exige para cerrar.',
        'body': '''
<h2>¿Por qué es difícil conseguir seguro en California?</h2>
<p>Las pérdidas por incendios forestales y el costo del reaseguro hicieron que varias aseguradoras grandes dejaran de aceptar pólizas nuevas desde 2023 o subieran sus tarifas. Para que regresen, el estado aprobó la "Estrategia de Seguros Sostenibles": las aseguradoras pueden usar modelos de catástrofe en sus tarifas a cambio de comprometerse a escribir más pólizas en zonas de riesgo.</p>

<h2>¿Qué es el California FAIR Plan?</h2>
<p>Es el seguro de último recurso para quien no consigue póliza en el mercado normal. Cubre principalmente incendio, así que normalmente se combina con una póliza complementaria (DIC) que cubre robo, responsabilidad civil y daños por agua. Desde el 15 de octubre de 2026 sus tarifas subieron en promedio 29.1%.</p>

<h2>¿Cambia el riesgo según la zona del Bay Area?</h2>
<p>Sí. Las casas en colinas con vegetación, como partes de los Oakland Hills o Montclair, suelen tener más dificultad para conseguir seguro que las casas en las planicies de ciudades como <a href="/areas/hayward/">Hayward</a>, <a href="/areas/concord/">Concord</a> o <a href="/areas/san-leandro/">San Leandro</a>. Antes de ofertar, pide una cotización con la dirección exacta.</p>

<h2>¿Necesito seguro contra terremotos?</h2>
<p>El seguro normal de casa no cubre terremotos. Se compra aparte, por ejemplo con pólizas de la California Earthquake Authority a través de tu aseguradora. Los deducibles suelen ir de 5% a 25% del valor asegurado. El banco normalmente no lo exige, pero en el Bay Area vale la pena considerarlo, sobre todo cerca de fallas como la de Hayward.</p>

<h2>¿Cómo puedes conseguir mejor precio?</h2>
<ul>
<li><strong>Cotiza temprano:</strong> en cuanto aceptan tu oferta, no la semana del cierre.</li>
<li><strong>Usa un agente de seguros independiente</strong> que trabaje con varias compañías.</li>
<li><strong>Pide al vendedor el reporte CLUE</strong>, el historial de reclamos de la casa.</li>
<li><strong>Protege la casa contra incendios:</strong> las reglas de California exigen que las aseguradoras den descuentos por medidas de mitigación, como limpiar la vegetación y usar respiraderos resistentes.</li>
<li><strong>Revisa el techo:</strong> un techo nuevo o resistente al fuego ayuda.</li>
<li><strong>Sube el deducible</strong> si tienes reservas, y combina el seguro de casa con el del carro.</li>
</ul>

<h2>¿Cómo afecta el seguro a cuánto puedes comprar?</h2>
<p>El banco suma el seguro a tu pago mensual al calcular tu relación deuda-ingreso. Un seguro caro puede bajar el precio máximo que te aprueban. Inclúyelo en tu presupuesto; mira <a href="/blog/cuanto-ganar-para-comprar-casa-bay-area/">cuánto tienes que ganar para comprar</a>.</p>
''',
        'faq': [
            ('¿El banco me exige seguro de casa?',
             'Sí. Para cerrar un préstamo necesitas un seguro que cubra al menos el daño a la vivienda. El seguro contra terremotos normalmente es opcional.'),
            ('¿Qué hago si mi aseguradora no renueva mi póliza?',
             'En California deben avisarte con al menos 75 días de anticipación. Busca otra póliza con un agente independiente y, si no consigues, el FAIR Plan. El Departamento de Seguros de California tiene una línea de ayuda: 1-800-927-4357.'),
            ('¿El FAIR Plan cubre todo?',
             'No. Cubre principalmente incendio y algunos daños relacionados. Para robo, responsabilidad civil y agua normalmente necesitas una póliza complementaria (DIC).'),
        ],
        'sources': [
            ('KQED: el FAIR Plan sube 29.1% en otoño de 2026', 'https://www.kqed.org/news/12094860/california-fair-plan-announces-29-1-rate-hike-for-homeowners-this-fall'),
            ('California FAIR Plan', 'https://www.cfpnet.com/'),
            ('Departamento de Seguros de California', 'https://www.insurance.ca.gov/'),
            ('California Earthquake Authority', 'https://www.earthquakeauthority.com/'),
        ],
    },
    {
        'slug': 'casa-heredada-california',
        'category': 'Vender',
        'title': 'Heredé una casa en California: ¿vender, rentar o quedarme? Impuestos, Prop 19 y probate (2026)',
        'seo_title': 'Heredé una casa en California: vender, rentar o quedarme',
        'desc': 'Qué hacer si heredaste una casa en California en 2026: probate o fideicomiso, cómo funciona la Prop 19 (exclusión hasta $1,044,586), el ajuste de base al heredar y cuándo conviene vender, rentar o vivir en ella.',
        'keywords': ['heredé una casa', 'casa heredada California', 'vender casa heredada', 'Prop 19 herencia', 'probate California'],
        'cities': ['oakland', 'hayward', 'san-leandro'],
        'related': ['impuesto-a-la-propiedad-california', 'cuanto-cuesta-vender-casa-california', 'cuanto-vale-mi-casa-bay-area'],
        'answer': 'Si heredaste una casa en California, primero hay que pasar el título a tu nombre: por probate si la casa no estaba en un fideicomiso, o directamente si estaba en un living trust. Por la Proposición 19, solo conservas el valor fiscal bajo de tus padres si haces de la casa tu residencia principal, y con un límite de $1,044,586 para transferencias hasta el 15 de febrero de 2027. Si la vendes pronto, el ajuste de base al heredar (step-up) suele dejar poca o ninguna ganancia sujeta a impuestos.',
        'body': '''
<h2>¿Cómo pasa la casa a tu nombre?</h2>
<table>
<thead><tr><th>Cómo estaba la casa</th><th>Qué se hace</th></tr></thead>
<tbody>
<tr><td>En un fideicomiso (living trust)</td><td>El fideicomisario la transfiere o la vende sin pasar por la corte</td></tr>
<tr><td>En "joint tenancy" con otra persona</td><td>Pasa al otro dueño con documentos del fallecimiento</td></tr>
<tr><td>Con escritura de transferencia al fallecer (TOD deed)</td><td>Pasa al beneficiario nombrado en la escritura</td></tr>
<tr><td>Solo a nombre de la persona fallecida, sin fideicomiso</td><td>Normalmente se necesita probate en la corte</td></tr>
</tbody>
</table>

<h2>¿Qué es el probate y cuánto tarda?</h2>
<p>Es el proceso en la corte para nombrar a un administrador, pagar deudas y repartir los bienes. Suele tardar muchos meses, a menudo más de un año, y la ley de California fija honorarios para el administrador y el abogado según el valor de la herencia. El procedimiento simplificado de "small estate" ($208,850 para fallecimientos desde el 1 de abril de 2025) aplica a bienes personales; para la casa, habla con un abogado de herencias.</p>
<p>Durante el probate sí se puede vender la casa, muchas veces con aviso a los herederos o con aprobación de la corte.</p>

<h2>¿Pagas impuestos si vendes la casa heredada?</h2>
<p>Por el ajuste de base (step-up), tu costo para el impuesto federal pasa a ser el valor de la casa en la fecha del fallecimiento, no lo que pagaron tus padres. Ejemplo: tus padres la compraron en $150,000 y valía $800,000 al fallecer. Si la vendes en $810,000, la ganancia es de unos $10,000, y con los costos de venta puede ser cero. California no tiene impuesto estatal a la herencia.</p>

<h2>¿Qué pasa con el impuesto a la propiedad?</h2>
<p>Por la Proposición 19, el valor fiscal de tus padres solo se conserva si la casa pasa a ser tu residencia principal y pides la exención de propietario dentro de un año. Además hay un límite: si el valor de mercado supera el valor fiscal de tus padres en más de $1,044,586 (para transferencias del 16 de febrero de 2025 al 15 de febrero de 2027), la diferencia se suma. Si no vives en ella, se vuelve a valorar al precio de mercado. Más en <a href="/blog/impuesto-a-la-propiedad-california/">impuesto a la propiedad en California</a>.</p>

<h2>¿Vender, rentar o quedarte?</h2>
<table>
<thead><tr><th>Opción</th><th>A favor</th><th>A considerar</th></tr></thead>
<tbody>
<tr><td>Vivir en ella</td><td>Puedes conservar el valor fiscal de tus padres (con límite)</td><td>Reparaciones pendientes y repartir con otros herederos</td></tr>
<tr><td>Rentarla</td><td>Ingreso mensual y posible plusvalía</td><td>El impuesto sube al valor de mercado; eres arrendador con obligaciones legales</td></tr>
<tr><td>Venderla</td><td>Dinero para repartir; el step-up reduce el impuesto</td><td>Costos de venta; ponerse de acuerdo entre herederos</td></tr>
</tbody>
</table>

<h2>¿Qué pasa si los hermanos no se ponen de acuerdo?</h2>
<p>Una opción es que un heredero compre la parte de los otros, con un préstamo o un refinanciamiento. Si no hay acuerdo, cualquiera de los dueños puede pedir a la corte una "partición", que normalmente termina en la venta. Negociar casi siempre sale más barato.</p>

<h2>¿Conviene vender la casa como está?</h2>
<p>Muchas casas heredadas necesitan trabajo. Puedes venderla "as is" o hacer arreglos pequeños que suban el precio. Un <a href="/blog/cuanto-vale-mi-casa-bay-area/">análisis comparativo de mercado</a> te muestra cuánto vale en cada escenario.</p>
''',
        'faq': [
            ('¿Hay impuesto a la herencia en California?',
             'No. California no tiene impuesto estatal a la herencia. El impuesto federal al patrimonio solo afecta herencias muy grandes, de más de $15 millones por persona en 2026.'),
            ('¿Qué pasa si la casa tenía una hipoteca inversa?',
             'La deuda se paga al vender. Si el saldo es mayor que el valor de la casa, los herederos pueden quedársela pagando el saldo o 95% del valor de tasación, lo que sea menor, o venderla.'),
            ('¿Tengo que asegurar la casa mientras está vacía?',
             'Sí. Muchas pólizas limitan la cobertura si la casa queda vacía mucho tiempo. Avisa a la aseguradora y pregunta por una póliza para casa desocupada.'),
        ],
        'sources': [
            ('BOE: Proposición 19', 'https://www.boe.ca.gov/prop19/'),
            ('BOE: ajuste de la exclusión de la Prop 19 (2025)', 'https://boe.ca.gov/news/2025/NR-25-02.htm'),
            ('IRS: Publicación 551, base de los bienes', 'https://www.irs.gov/publications/p551'),
            ('Cortes de California: ayuda con herencias (probate)', 'https://selfhelp.courts.ca.gov/probate'),
        ],
    },
    {
        'slug': 'adu-california',
        'category': 'Invertir',
        'title': 'Construir un ADU en California (2026): reglas, permisos y cómo puede ayudarte a pagar tu casa',
        'seo_title': 'Construir un ADU en California (2026): reglas y permisos',
        'desc': 'Guía 2026 para construir un ADU o JADU en tu casa en California: qué permite la ley estatal, permisos en 60 días, sin cuotas de impacto bajo 750 pies cuadrados, cómo financiarlo y cómo afecta impuestos y valor.',
        'keywords': ['ADU California', 'construir ADU', 'convertir garaje en casa', 'JADU', 'unidad adicional para rentar'],
        'cities': ['oakland', 'concord', 'hayward', 'san-leandro'],
        'related': ['fix-and-flip-bay-area-regla-70', 'rentar-o-comprar-casa-bay-area', 'impuesto-a-la-propiedad-california'],
        'answer': 'En California casi cualquier casa unifamiliar puede agregar un ADU (una unidad adicional, como una casita en el patio o un garaje convertido) y además un JADU de hasta 500 pies cuadrados dentro de la casa. La ciudad debe aprobar o negar una solicitud completa en 60 días, no puede exigir que vivas en la propiedad para tener un ADU y no cobra cuotas de impacto por ADUs de menos de 750 pies cuadrados. En el Bay Area es una forma común de generar renta o de vivir cerca de la familia.',
        'body': '''
<h2>¿Qué tipos de ADU hay?</h2>
<table>
<thead><tr><th>Tipo</th><th>Qué es</th><th>Lo que debes saber</th></tr></thead>
<tbody>
<tr><td>ADU separado</td><td>Una casita nueva en el patio</td><td>La opción más cara, pero la más independiente</td></tr>
<tr><td>ADU adjunto</td><td>Una ampliación pegada a la casa</td><td>Con entrada propia</td></tr>
<tr><td>Garaje convertido</td><td>El garaje se vuelve vivienda</td><td>Suele ser más barato; no tienes que reponer el estacionamiento</td></tr>
<tr><td>JADU</td><td>Hasta 500 pies cuadrados dentro de la casa</td><td>El dueño debe vivir en la casa principal o en el JADU</td></tr>
</tbody>
</table>

<h2>¿Qué permite la ley estatal?</h2>
<ul>
<li>La ciudad debe aprobar o negar una solicitud completa en 60 días.</li>
<li>No pueden exigir que el dueño viva en la propiedad para tener un ADU.</li>
<li>No se cobran cuotas de impacto por ADUs de menos de 750 pies cuadrados.</li>
<li>Las distancias a los lados y atrás no pueden ser mayores de 4 pies.</li>
<li>Las ciudades deben permitir al menos un ADU de 800 pies cuadrados, aunque sus reglas sean más estrictas.</li>
<li>No se exige estacionamiento extra en muchos casos, por ejemplo a media milla del transporte público.</li>
</ul>
<p>Cada ciudad tiene su propia ordenanza, pero no puede ser más restrictiva que la ley estatal. El manual de ADU 2026 de HCD, disponible en español, explica todo con detalle.</p>

<h2>¿Cuáles son los pasos?</h2>
<ol>
<li>Revisa la zonificación, el tamaño del lote y las conexiones de agua, drenaje y electricidad.</li>
<li>Pregunta si tu ciudad tiene planos de ADU preaprobados; ahorran tiempo y dinero.</li>
<li>Prepara planos con un diseñador o arquitecto y pide cotizaciones a contratistas con licencia.</li>
<li>Solicita el permiso; la ciudad tiene 60 días para responder a una solicitud completa.</li>
<li>Construye con inspecciones de la ciudad y obtén el certificado final.</li>
</ol>

<h2>¿Cómo se financia un ADU?</h2>
<ul>
<li>Ahorros o una línea de crédito sobre el valor de tu casa (HELOC).</li>
<li>Refinanciamiento con retiro de efectivo.</li>
<li>Préstamos de renovación que prestan según el valor después de la obra.</li>
<li>Si vas a comprar, algunos programas permiten contar parte de la renta del ADU como ingreso. Lee <a href="/blog/cuanto-ganar-para-comprar-casa-bay-area/">cuánto tienes que ganar para comprar</a>.</li>
</ul>

<h2>¿Cómo afecta el impuesto y el valor de la casa?</h2>
<p>Solo se vuelve a valorar el valor agregado por el ADU; el resto de la casa mantiene su valor de la Proposición 13. Un ADU con permiso suele subir el valor de la casa y atrae a compradores que buscan renta o espacio para la familia. Normalmente el ADU no se puede vender por separado, aunque algunas ciudades empiezan a permitirlo.</p>

<h2>¿Conviene en una inversión o un Fix & Flip?</h2>
<p>Agregar un ADU puede subir el valor de reventa (ARV) y hacer que los números de un proyecto funcionen. También alarga el tiempo de obra, así que inclúyelo en tu análisis. Ve <a href="/blog/fix-and-flip-bay-area-regla-70/">cómo calcular un Fix & Flip</a>.</p>
''',
        'faq': [
            ('¿Necesito permiso para convertir mi garaje en vivienda?',
             'Sí. Una conversión sin permiso puede generar multas, problemas con el seguro y complicaciones al vender. La ley estatal hace que el permiso de un ADU sea más fácil y rápido que antes.'),
            ('¿Puedo legalizar una unidad que ya construí sin permiso?',
             'En muchos casos sí. La ley de California da facilidades para legalizar unidades construidas sin permiso antes de 2020, mientras no haya riesgos graves de salud o seguridad.'),
            ('¿Puedo rentar el ADU?',
             'Sí. Puedes rentarlo a largo plazo; muchas ciudades prohíben rentas de menos de 30 días. Al rentarlo, sigues las leyes de inquilinos de tu ciudad.'),
        ],
        'sources': [
            ('HCD: manual de ADU 2026 (en español, PDF)', 'https://www.hcd.ca.gov/sites/default/files/docs/policy-and-research/2026-adu-handbook-es.pdf'),
            ('HCD: unidades de vivienda accesorias (ADU)', 'https://www.hcd.ca.gov/policy-and-research/accessory-dwelling-units'),
        ],
    },
]

# Home page "Guías" section, in this order.
FEATURED = ['comprar-casa-con-itin-california', 'programas-primera-casa-california', 'cuanto-vale-mi-casa-bay-area']
