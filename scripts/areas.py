"""City landing pages: content and photo credits. scripts/build.py renders these.

Facts (BART stations, freeways, neighborhoods, census shares) were checked against
the cities' Wikipedia articles in Oct 2026. Keep claims about Alejandra's own work
limited to what the home page already states.
"""

COUNTIES = {
    'alameda': {'es': 'Condado de Alameda', 'en': 'Alameda County'},
    'contra-costa': {'es': 'Condado de Contra Costa', 'en': 'Contra Costa County'},
    'san-francisco': {'es': 'San Francisco', 'en': 'San Francisco'},
}

# Closed deals shown on the home page (same photos, same data).
PROPERTIES = {
    'hillcrest': {'img': '2-hillcrest-ct-san-anselmo.webp', 'addr': '2 Hillcrest Ct', 'city': 'San Anselmo, CA',
                  'price': '$1,200,000', 'type': {'es': 'Residencial', 'en': 'Residential'}},
    'hyde': {'img': '3228-hyde-st-oakland.webp', 'addr': '3228 Hyde St', 'city': 'Oakland, CA',
             'price': '$700,000', 'type': {'es': 'Fix & Flip', 'en': 'Fix & Flip'}},
    'dover': {'img': '5614-dover-st-oakland.webp', 'addr': '5614 Dover St', 'city': 'Oakland, CA',
              'price': '$950,000', 'type': {'es': 'Fix & Flip', 'en': 'Fix & Flip'}},
    '57th': {'img': '2311-57th-ave-oakland.webp', 'addr': '2311 57th Ave', 'city': 'Oakland, CA',
             'price': '$725,000', 'type': {'es': 'Residencial', 'en': 'Residential'}},
    '27th': {'img': '672-27th-ave-oakland.webp', 'addr': '672 27th Ave', 'city': 'Oakland, CA',
             'price': '$680,000', 'type': {'es': 'Fix & Flip', 'en': 'Fix & Flip'}},
}
RECENT = ['hillcrest', 'hyde', 'dover']

CITIES = [
    {
        'slug': 'oakland', 'name': 'Oakland', 'county': 'alameda',
        'near': ['san-leandro', 'hayward', 'san-francisco', 'richmond', 'walnut-creek'],
        'work': ['hyde', 'dover', '57th', '27th'],
        'photo': {'file': 'oakland.webp', 'author': 'Robert Hsiao', 'license': 'CC BY-SA 4.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/4.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Lake_Merritt_2022-06-16.png'},
        'es': {
            'desc': 'Realtor que habla español en Oakland, CA. Compra, venta e inversión en Fruitvale, East Oakland, Rockridge y más. Cuatro ventas recientes en Oakland. Escríbeme por WhatsApp.',
            'alt': 'Vista aérea de Lake Merritt y el centro de Oakland',
            'lead': 'Compra, venta e inversión en Oakland con una agente que habla tu idioma. Aquí están cuatro de mis ventas más recientes, tres de ellas proyectos Fix & Flip.',
            'card': 'Fruitvale, Rockridge, Montclair y East Oakland. Mis cierres más recientes.',
            'intro': [
                'Oakland es el corazón del East Bay y una de las ciudades más diversas de California. Su oferta va desde casas Craftsman y victorianas en el norte de la ciudad hasta bungalows y casas de un piso en East Oakland, muchas con potencial de remodelación.',
                'Cuatro de mis ventas recientes están en Oakland, así que conozco de cerca cómo cambian los precios de un barrio a otro, qué remodelaciones suman valor y cómo negociar cuando hay varias ofertas.',
            ],
            'facts': [
                ('Condado', 'Alameda'),
                ('BART', 'Fruitvale, Coliseum, Lake Merritt, 12th St, 19th St, MacArthur, Rockridge y West Oakland'),
                ('Autopistas', 'I-880, I-580, I-980, SR-24 y SR-13'),
                ('Tipo de casas', 'Craftsman, victorianas, bungalows y condominios'),
            ],
            'hoods': [
                ('Fruitvale', 'Centro de la comunidad latina de Oakland, con negocios en International Boulevard y estación de BART propia.'),
                ('Rockridge y Temescal', 'Calles caminables, casas Craftsman y mucha demanda. Las casas bien presentadas se venden rápido.'),
                ('Montclair', 'En las colinas, junto a la autopista 13: casas con vista, lotes más grandes y ambiente de pueblo.'),
                ('Laurel y Dimond', 'Barrios residenciales y familiares con comercios locales, entre las planicies y las colinas.'),
                ('East Oakland', 'Las casas más accesibles de la ciudad y buenas oportunidades para comprar y remodelar.'),
                ('Lake Merritt y Grand Lake', 'Condominios y departamentos cerca del lago, del centro y del BART.'),
            ],
            'why': [
                ('Conexión', 'Llegas a San Francisco en minutos por BART o por el Bay Bridge.'),
                ('Variedad', 'Desde condominios hasta casas en las colinas: hay opciones para muchos presupuestos.'),
                ('Inversión', 'Muchas casas antiguas tienen potencial de remodelación; así trabajé mis proyectos Fix & Flip aquí.'),
            ],
            'faq': [
                ('¿Conviene comprar una casa para remodelar en Oakland?',
                 'Puede convenir si los números cierran. Antes de ofertar calculamos el precio de compra, el costo y el tiempo de la remodelación, y un precio de reventa realista con ventas comparables del barrio.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Oakland, CA. Buying, selling and investing in Fruitvale, East Oakland, Rockridge and beyond, with four recent Oakland sales. Message me on WhatsApp.',
            'alt': 'Aerial view of Lake Merritt and downtown Oakland',
            'lead': 'Buy, sell or invest in Oakland with an agent who speaks English and Spanish. Four of my most recent sales are here, three of them Fix & Flip projects.',
            'card': 'Fruitvale, Rockridge, Montclair and East Oakland. My most recent closings.',
            'intro': [
                "Oakland is the heart of the East Bay and one of California's most diverse cities. Homes range from Craftsman and Victorian houses in North Oakland to bungalows and single-story homes in East Oakland, many with renovation potential.",
                'Four of my recent sales are in Oakland, so I know how prices shift from one neighborhood to the next, which upgrades add value, and how to negotiate when there are multiple offers.',
            ],
            'facts': [
                ('County', 'Alameda'),
                ('BART', 'Fruitvale, Coliseum, Lake Merritt, 12th St, 19th St, MacArthur, Rockridge and West Oakland'),
                ('Freeways', 'I-880, I-580, I-980, SR-24 and SR-13'),
                ('Housing', 'Craftsman, Victorian, bungalows and condos'),
            ],
            'hoods': [
                ('Fruitvale', "The center of Oakland's Latino community, with International Boulevard businesses and its own BART station."),
                ('Rockridge & Temescal', 'Walkable streets, Craftsman homes and strong demand. Well-presented homes sell fast.'),
                ('Montclair', 'In the hills along Highway 13: view homes, larger lots and a village feel.'),
                ('Laurel & Dimond', 'Family-friendly residential neighborhoods with local shops, between the flats and the hills.'),
                ('East Oakland', 'The most affordable homes in the city and good buy-and-renovate opportunities.'),
                ('Lake Merritt & Grand Lake', 'Condos and apartments near the lake, downtown and BART.'),
            ],
            'why': [
                ('Access', 'San Francisco is minutes away by BART or the Bay Bridge.'),
                ('Range', 'From condos to hillside homes, there are options for many budgets.'),
                ('Investment', "Many older homes have renovation upside; that's how I approached my Fix & Flip projects here."),
            ],
            'faq': [
                ('Is it worth buying a fixer-upper in Oakland?',
                 'It can be, if the numbers work. Before making an offer we run the purchase price, renovation cost and timeline, and a realistic resale price based on comparable sales in the neighborhood.'),
            ],
        },
    },
    {
        'slug': 'san-francisco', 'name': 'San Francisco', 'county': 'san-francisco',
        'near': ['oakland', 'richmond', 'san-leandro'],
        'photo': {'file': 'san-francisco.webp', 'author': 'King of Hearts', 'license': 'CC BY-SA 3.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/3.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Painted_Ladies_San_Francisco_January_2013_003.jpg'},
        'es': {
            'desc': 'Realtor que habla español en San Francisco, CA. Te ayudo a comprar o vender en la Misión, el Excelsior, Bernal Heights y más: casas, condominios y TIC. Escríbeme por WhatsApp.',
            'alt': 'Las Painted Ladies frente al skyline de San Francisco',
            'lead': 'San Francisco es uno de los mercados más caros y competitivos del país. Te acompaño en español para que compres o vendas con estrategia.',
            'card': 'La Misión, Excelsior, Bernal Heights y el Sunset. Casas, condominios y TIC.',
            'intro': [
                'En San Francisco conviven casas victorianas y edwardianas, condominios modernos y propiedades TIC (tenancy-in-common). Cada tipo tiene reglas y opciones de financiamiento distintas, y elegir bien cambia mucho el resultado.',
                'La comunidad latina tiene raíces profundas en la Misión y el Excelsior. Si buscas tu primera casa o un condominio, te ayudo a entender qué te conviene y a preparar una oferta que compita.',
            ],
            'facts': [
                ('Condado', 'Ciudad y Condado de San Francisco'),
                ('BART', '16th St Mission, 24th St Mission, Glen Park, Balboa Park y el centro'),
                ('Transporte', 'BART, Muni y Caltrain'),
                ('Tipo de vivienda', 'Victorianas, edwardianas, condominios y TIC'),
            ],
            'hoods': [
                ('La Misión', 'El barrio latino histórico de la ciudad, con el Distrito Cultural Latino de la Calle 24 y dos estaciones de BART.'),
                ('Excelsior', 'Al sur de la ciudad y de los barrios más diversos, con casas unifamiliares y ambiente de barrio.'),
                ('Bernal Heights', 'Casas en la colina junto a la Misión, con calles tranquilas y vistas.'),
                ('Bayview', 'Una de las zonas más accesibles dentro de la ciudad, con nuevos desarrollos.'),
                ('Sunset', 'Casas cerca del mar y de Golden Gate Park, populares entre familias.'),
                ('Noe Valley', 'Familiar y muy buscado, con comercios en la calle 24 y casas de mayor precio.'),
            ],
            'why': [
                ('Valor a largo plazo', 'La demanda de vivienda en San Francisco se mantiene alta año tras año.'),
                ('Programas locales', 'La ciudad ofrece programas para compradores de primera vivienda a través de su Oficina de Vivienda (MOHCD); te oriento para revisar si calificas.'),
                ('Transporte', 'Con BART, Muni y Caltrain puedes vivir bien sin depender del auto.'),
            ],
            'faq': [
                ('¿Qué es una propiedad TIC en San Francisco?',
                 'En un TIC compras una parte de un edificio junto con otros dueños y tienes derecho a usar una unidad específica. Suele costar menos que un condominio, pero el financiamiento y las reglas son distintos. Te explico los pros y contras antes de ofertar.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in San Francisco, CA. Buy or sell in the Mission, Excelsior, Bernal Heights and beyond: houses, condos and TICs. Message me on WhatsApp.',
            'alt': 'The Painted Ladies in front of the San Francisco skyline',
            'lead': "San Francisco is one of the most expensive, competitive markets in the country. I'll guide you in English or Spanish so you buy or sell with a strategy.",
            'card': 'The Mission, Excelsior, Bernal Heights and the Sunset. Houses, condos and TICs.',
            'intro': [
                'San Francisco mixes Victorian and Edwardian homes, modern condos and TIC (tenancy-in-common) properties. Each type comes with different rules and financing options, and choosing well changes the outcome.',
                "The city's Latino community has deep roots in the Mission and the Excelsior. If you're looking for your first home or a condo, I'll help you understand what fits and put together an offer that competes.",
            ],
            'facts': [
                ('County', 'City and County of San Francisco'),
                ('BART', '16th St Mission, 24th St Mission, Glen Park, Balboa Park and downtown'),
                ('Transit', 'BART, Muni and Caltrain'),
                ('Housing', 'Victorian, Edwardian, condos and TICs'),
            ],
            'hoods': [
                ('The Mission', "The city's historic Latino neighborhood, home to the Calle 24 Latino Cultural District and two BART stations."),
                ('Excelsior', 'On the south side and one of the most diverse neighborhoods, with single-family homes and a neighborhood feel.'),
                ('Bernal Heights', 'Hillside homes next to the Mission, with quiet streets and views.'),
                ('Bayview', 'One of the more affordable areas within the city, with new development.'),
                ('Sunset', 'Homes near the ocean and Golden Gate Park, popular with families.'),
                ('Noe Valley', 'Family-oriented and in high demand, with 24th Street shops and higher price points.'),
            ],
            'why': [
                ('Long-term value', 'Housing demand in San Francisco stays strong year after year.'),
                ('Local programs', "The city offers first-time buyer programs through its housing office (MOHCD); I'll help you check whether you qualify."),
                ('Transit', 'With BART, Muni and Caltrain you can live well without relying on a car.'),
            ],
            'faq': [
                ('What is a TIC in San Francisco?',
                 "With a TIC you buy a share of a building together with other owners and get the right to use a specific unit. It's usually cheaper than a condo, but financing and rules differ. I'll walk you through the pros and cons before you make an offer."),
            ],
        },
    },
    {
        'slug': 'pittsburg', 'name': 'Pittsburg', 'county': 'contra-costa',
        'near': ['antioch', 'concord', 'brentwood', 'walnut-creek'],
        'photo': {'file': 'pittsburg.webp', 'author': 'Armenshirazd', 'license': 'CC BY 4.0',
                  'license_url': 'https://creativecommons.org/licenses/by/4.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Old_Town_Pittsburg,_Pittsburg_California.jpg'},
        'es': {
            'desc': 'Realtor que habla español en Pittsburg, CA. Casas más accesibles, dos estaciones de BART y una comunidad latina fuerte. Te ayudo a comprar, vender o invertir. Escríbeme.',
            'alt': 'Old Town Pittsburg, California',
            'lead': 'Pittsburg es de las ciudades más accesibles del East Bay, con dos estaciones de BART y una comunidad latina muy fuerte. Te ayudo a comprar, vender o invertir, en español.',
            'card': 'Old Town, la marina y dos estaciones de BART. Precios más accesibles.',
            'intro': [
                'Junto a la bahía de Suisun, Pittsburg pasó de ser un pueblo minero y pesquero, cuyo nombre original fue Black Diamond, a una ciudad de familias que viajan a trabajar por la autopista 4 o en BART.',
                'Cerca de 4 de cada 10 residentes son latinos, y hay opciones para distintos presupuestos: casas de mediados del siglo pasado cerca de Old Town y desarrollos más nuevos hacia el sur de la ciudad.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('BART', 'Pittsburg/Bay Point y Pittsburg Center'),
                ('Autopista', 'SR-4, que cruza la ciudad de oeste a este'),
                ('Educación', 'Los Medanos College'),
            ],
            'hoods': [
                ('Old Town y la marina', 'El centro histórico sobre Railroad Avenue, junto al agua, con eventos, restaurantes y la marina.'),
                ('Cerca de Pittsburg Center', 'Ideal si viajas en BART: la estación está en Railroad Avenue y la autopista 4.'),
                ('Sur de Pittsburg', 'Casas más nuevas hacia las colinas, cerca del parque regional Black Diamond Mines.'),
                ('Oeste, junto a Bay Point', 'Acceso rápido al BART Pittsburg/Bay Point y a la autopista 4.'),
            ],
            'why': [
                ('Precio', 'Más espacio por tu dinero que en Oakland o San Francisco.'),
                ('BART', 'Dos estaciones dentro de la ciudad, con conexión directa a Oakland y San Francisco.'),
                ('Comunidad', 'Una comunidad latina grande, con negocios y servicios en español.'),
            ],
            'faq': [
                ('¿Es buena idea comprar mi primera casa en Pittsburg?',
                 'Para muchas familias sí: los precios suelen ser más accesibles que en el centro del Bay Area y hay BART. Revisamos tu presupuesto, tu ruta al trabajo y los programas de primera vivienda de California (CalHFA) que podrían aplicar.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Pittsburg, CA. More affordable homes, two BART stations and a strong Latino community. I help you buy, sell or invest. Message me on WhatsApp.',
            'alt': 'Old Town Pittsburg, California',
            'lead': 'Pittsburg is one of the more affordable cities in the East Bay, with two BART stations and a strong Latino community. I help you buy, sell or invest, in English or Spanish.',
            'card': 'Old Town, the marina and two BART stations. More affordable prices.',
            'intro': [
                'On Suisun Bay, Pittsburg grew from a mining and fishing town, originally named Black Diamond, into a city of families who commute on Highway 4 or BART.',
                'About 4 in 10 residents are Latino, and there are options for different budgets: mid-century homes near Old Town and newer developments toward the south of the city.',
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('BART', 'Pittsburg/Bay Point and Pittsburg Center'),
                ('Freeway', 'SR-4, crossing the city west to east'),
                ('Education', 'Los Medanos College'),
            ],
            'hoods': [
                ('Old Town & the marina', 'The historic downtown along Railroad Avenue by the water, with events, restaurants and the marina.'),
                ('Near Pittsburg Center', 'Ideal if you commute by BART: the station sits at Railroad Avenue and Highway 4.'),
                ('South Pittsburg', 'Newer homes toward the hills, near Black Diamond Mines Regional Preserve.'),
                ('West, by Bay Point', 'Quick access to Pittsburg/Bay Point BART and Highway 4.'),
            ],
            'why': [
                ('Price', 'More space for your money than in Oakland or San Francisco.'),
                ('BART', 'Two stations in town, with direct trains to Oakland and San Francisco.'),
                ('Community', 'A large Latino community with Spanish-speaking businesses and services.'),
            ],
            'faq': [
                ('Is Pittsburg a good place to buy a first home?',
                 'For many families, yes: prices tend to be lower than in the central Bay Area and there is BART. We review your budget, your commute and the California first-time buyer programs (CalHFA) that may apply.'),
            ],
        },
    },
    {
        'slug': 'antioch', 'name': 'Antioch', 'county': 'contra-costa',
        'near': ['pittsburg', 'brentwood', 'concord'],
        'photo': {'file': 'antioch.webp', 'author': 'Pi.1415926535', 'license': 'CC BY-SA 3.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/3.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Antioch_aerial_view,_August_2018_(cropped).JPG'},
        'es': {
            'desc': 'Realtor que habla español en Antioch, CA. Casas amplias a precios más accesibles, BART y el río San Joaquín. Te ayudo a comprar, vender o invertir. Escríbeme por WhatsApp.',
            'alt': 'Vista aérea de Antioch y el río San Joaquín',
            'lead': 'Antioch, a orillas del río San Joaquín, ofrece casas amplias a precios más accesibles y conexión directa a BART. Te ayudo en español a comprar, vender o invertir.',
            'card': 'Rivertown, Deer Valley y Lone Tree. Casas amplias y BART desde 2018.',
            'intro': [
                'Es una de las ciudades más grandes del este de Contra Costa. Desde 2018 tiene estación de BART, lo que la conectó directamente con Oakland, San Francisco y el aeropuerto SFO.',
                'Más de un tercio de sus residentes son latinos. Hay casas de distintas épocas: el centro histórico de Rivertown, barrios de las últimas décadas del siglo pasado y desarrollos más nuevos al sureste, en Deer Valley y Lone Tree.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('BART', 'Estación Antioch (eBART)'),
                ('Autopistas', 'SR-4 y SR-160 (puente de Antioch hacia el Delta)'),
                ('Parques', 'Contra Loma y Black Diamond Mines'),
            ],
            'hoods': [
                ('Rivertown', 'El centro histórico junto al río, con el teatro El Campanil y edificios de principios del siglo XX.'),
                ('Deer Valley', 'Casas más nuevas y amplias en el sur de la ciudad, cerca de escuelas y parques.'),
                ('Lone Tree', 'Zona residencial y comercial en el sureste, con acceso rápido a la autopista 4.'),
                ('Contra Loma', 'Barrios junto al parque regional y su lago, ideales para familias que buscan naturaleza.'),
            ],
            'why': [
                ('Espacio', 'Casas y terrenos más grandes por el mismo presupuesto que en el centro del Bay Area.'),
                ('BART', 'La estación de Antioch te conecta sin transbordos con Oakland y San Francisco.'),
                ('Naturaleza', 'El Delta, Contra Loma y Black Diamond Mines están a minutos.'),
            ],
            'faq': [
                ('¿Antioch es buena zona para invertir en una casa de renta?',
                 'Puede serlo: los precios de compra son más bajos que en el centro del Bay Area y hay demanda de renta. Antes de comprar analizamos la renta esperada, impuestos, seguro y reparaciones para ver si el número te funciona.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Antioch, CA. Spacious homes at more affordable prices, BART and the San Joaquin River. I help you buy, sell or invest. Message me on WhatsApp.',
            'alt': 'Aerial view of Antioch and the San Joaquin River',
            'lead': 'Antioch, on the San Joaquin River, offers spacious homes at more affordable prices and a direct BART connection. I help you buy, sell or invest, in English or Spanish.',
            'card': 'Rivertown, Deer Valley and Lone Tree. Spacious homes and BART since 2018.',
            'intro': [
                'One of the largest cities in East Contra Costa, Antioch got its BART station in 2018, connecting it directly to Oakland, San Francisco and SFO.',
                'More than a third of residents are Latino. Homes span several eras: historic Rivertown downtown, late-20th-century neighborhoods and newer developments to the southeast in Deer Valley and Lone Tree.',
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('BART', 'Antioch station (eBART)'),
                ('Freeways', 'SR-4 and SR-160 (Antioch Bridge to the Delta)'),
                ('Parks', 'Contra Loma and Black Diamond Mines'),
            ],
            'hoods': [
                ('Rivertown', 'The historic downtown by the river, with El Campanil Theatre and early-1900s buildings.'),
                ('Deer Valley', 'Newer, larger homes in the south of the city, near schools and parks.'),
                ('Lone Tree', 'A residential and retail area in the southeast with quick Highway 4 access.'),
                ('Contra Loma', 'Neighborhoods next to the regional park and its lake, great for families who love the outdoors.'),
            ],
            'why': [
                ('Space', 'Bigger homes and lots for the same budget as the central Bay Area.'),
                ('BART', 'Antioch station connects you to Oakland and San Francisco with no transfers.'),
                ('Outdoors', 'The Delta, Contra Loma and Black Diamond Mines are minutes away.'),
            ],
            'faq': [
                ('Is Antioch a good area for a rental property?',
                 'It can be: purchase prices are lower than in the central Bay Area and there is rental demand. Before buying we analyze expected rent, taxes, insurance and repairs to see if the numbers work for you.'),
            ],
        },
    },
    {
        'slug': 'walnut-creek', 'name': 'Walnut Creek', 'county': 'contra-costa',
        'near': ['concord', 'pittsburg', 'oakland'],
        'photo': {'file': 'walnut-creek.webp', 'author': 'Pi.1415926535', 'license': 'CC BY-SA 3.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/3.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Walnut_Creek_panorama_from_hill,_August_2018.jpg'},
        'es': {
            'desc': 'Realtor que habla español en Walnut Creek, CA. Northgate, Parkmead, Tice Valley, Rossmoor y el centro. Estrategia para comprar o vender en un mercado de alta demanda.',
            'alt': 'Panorámica de Walnut Creek con el Monte Diablo al fondo',
            'lead': 'Walnut Creek combina un centro con tiendas y restaurantes, buenas escuelas y vistas al Monte Diablo. Te acompaño en español en un mercado de alta demanda.',
            'card': 'Northgate, Parkmead, Tice Valley y Rossmoor. Alta demanda y buenas escuelas.',
            'intro': [
                'Walnut Creek está en el corazón de Contra Costa, entre los valles de San Ramón y de Ygnacio, al pie del Monte Diablo. Tiene BART y acceso a la I-680 y la autopista 24 hacia Oakland y San Francisco.',
                'Es un mercado más caro y competitivo: aquí la preparación de la oferta y la estrategia de negociación hacen la diferencia. Si vas a vender, la presentación de la casa también.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('BART', 'Walnut Creek, y Pleasant Hill/Contra Costa Centre muy cerca'),
                ('Autopistas', 'I-680 y SR-24'),
                ('Escuelas', 'Según la dirección: Walnut Creek, Mt. Diablo, Lafayette o San Ramon Valley'),
            ],
            'hoods': [
                ('Centro', 'Condominios y townhomes a pasos de BART, Broadway Plaza y los restaurantes.'),
                ('Northgate', 'Casas unifamiliares al pie del Monte Diablo, muy buscadas por familias.'),
                ('Parkmead', 'Un barrio tradicional y unido, con casas de un piso y calles tranquilas.'),
                ('Tice Valley', 'Más rural y arbolado, con casas en lotes amplios.'),
                ('Rossmoor', 'Comunidad para mayores de 55 años, con unos 10,000 residentes y servicios propios.'),
            ],
            'why': [
                ('Calidad de vida', 'Centro caminable, parques y senderos del Monte Diablo.'),
                ('Ubicación', 'BART, I-680 y la autopista 24 te conectan con todo el Bay Area.'),
                ('Demanda estable', 'Compradores de todo el Bay Area buscan casa aquí año tras año.'),
            ],
            'faq': [
                ('¿Qué distrito escolar le toca a una casa en Walnut Creek?',
                 'Depende de la dirección exacta: una casa de Walnut Creek puede pertenecer a los distritos de Walnut Creek, Mt. Diablo, Lafayette o San Ramon Valley. Si las escuelas son prioridad, lo verificamos antes de ofertar.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Walnut Creek, CA. Northgate, Parkmead, Tice Valley, Rossmoor and downtown. A clear strategy to buy or sell in a high-demand market.',
            'alt': 'Panorama of Walnut Creek with Mount Diablo in the background',
            'lead': "Walnut Creek pairs a lively downtown with good schools and views of Mount Diablo. I'll guide you in English or Spanish through a high-demand market.",
            'card': 'Northgate, Parkmead, Tice Valley and Rossmoor. High demand and good schools.',
            'intro': [
                'Walnut Creek sits in the heart of Contra Costa, between the San Ramon and Ygnacio valleys at the foot of Mount Diablo. It has BART plus I-680 and Highway 24 toward Oakland and San Francisco.',
                "It's a pricier, competitive market: offer preparation and negotiation strategy make the difference here. If you're selling, so does how the home is presented.",
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('BART', 'Walnut Creek, with Pleasant Hill/Contra Costa Centre close by'),
                ('Freeways', 'I-680 and SR-24'),
                ('Schools', 'Depending on the address: Walnut Creek, Mt. Diablo, Lafayette or San Ramon Valley'),
            ],
            'hoods': [
                ('Downtown', 'Condos and townhomes steps from BART, Broadway Plaza and restaurants.'),
                ('Northgate', 'Single-family homes at the foot of Mount Diablo, popular with families.'),
                ('Parkmead', 'A classic, close-knit neighborhood with single-story homes and quiet streets.'),
                ('Tice Valley', 'More rural and wooded, with homes on generous lots.'),
                ('Rossmoor', 'A 55+ community of about 10,000 residents with its own amenities.'),
            ],
            'why': [
                ('Quality of life', 'A walkable downtown, parks and Mount Diablo trails.'),
                ('Location', 'BART, I-680 and Highway 24 connect you to the whole Bay Area.'),
                ('Steady demand', 'Buyers from across the Bay Area look for homes here year after year.'),
            ],
            'faq': [
                ('Which school district does a Walnut Creek home belong to?',
                 "It depends on the exact address: a Walnut Creek home can fall in the Walnut Creek, Mt. Diablo, Lafayette or San Ramon Valley districts. If schools are a priority, we'll confirm before making an offer."),
            ],
        },
    },
    {
        'slug': 'concord', 'name': 'Concord', 'county': 'contra-costa',
        'near': ['walnut-creek', 'pittsburg', 'antioch'],
        'photo': {'file': 'concord.webp', 'author': 'Geraoma', 'license': 'Dominio público',
                  'license_url': '',
                  'source': 'https://commons.wikimedia.org/wiki/File:Todos_Santos_Plaza_(Concord,_California)_Dec_2009.jpg'},
        'es': {
            'desc': 'Realtor que habla español en Concord, CA. Todos Santos Plaza, Monument, Clayton Valley e Ygnacio Valley. Dos estaciones de BART. Te ayudo a comprar, vender o invertir.',
            'alt': 'Todos Santos Plaza en el centro de Concord',
            'lead': 'Concord es la ciudad más grande de Contra Costa: casas para distintos presupuestos, dos estaciones de BART y una comunidad latina muy presente. Te ayudo en español.',
            'card': 'Todos Santos Plaza, Monument, Clayton e Ygnacio Valley. Dos estaciones de BART.',
            'intro': [
                'Su centro gira alrededor de Todos Santos Plaza, con mercado de agricultores, conciertos de verano y restaurantes. Cerca de la plaza y del BART se han construido nuevos departamentos y condominios.',
                'La zona de Monument Boulevard concentra una comunidad latina grande, con negocios y servicios en español. En los valles de Clayton e Ygnacio hay barrios residenciales de casas unifamiliares.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('BART', 'Concord y North Concord/Martinez'),
                ('Autopistas', 'I-680, SR-4 y SR-242'),
                ('Centro', 'Todos Santos Plaza'),
            ],
            'hoods': [
                ('Centro y Todos Santos', 'Condominios y casas cerca de la plaza, el BART y los restaurantes.'),
                ('Monument', 'Corredor de Monument Boulevard, con una comunidad latina grande y precios más accesibles.'),
                ('Clayton Valley', 'Casas unifamiliares en el este de la ciudad, rumbo a Clayton y el Monte Diablo.'),
                ('Ygnacio Valley', 'Barrios residenciales tranquilos sobre Ygnacio Valley Road, cerca de Walnut Creek.'),
                ('North Concord', 'Cerca del BART North Concord/Martinez y la autopista 4.'),
            ],
            'why': [
                ('Ubicación central', 'I-680, la autopista 4 y dos estaciones de BART.'),
                ('Variedad de precios', 'Desde condominios hasta casas unifamiliares en los valles.'),
                ('Comunidad', 'Negocios y servicios en español, sobre todo en la zona de Monument.'),
            ],
            'faq': [
                ('¿Concord es buena opción si trabajo en Walnut Creek, Oakland o San Francisco?',
                 'Sí, por eso muchos compradores la eligen: está junto a Walnut Creek y Pleasant Hill, y en BART llegas a Oakland y San Francisco sin cambiar de línea.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Concord, CA. Todos Santos Plaza, Monument, Clayton Valley and Ygnacio Valley, with two BART stations. I help you buy, sell or invest.',
            'alt': 'Todos Santos Plaza in downtown Concord',
            'lead': 'Concord is the largest city in Contra Costa County: homes for different budgets, two BART stations and a strong Latino community. I help you in English or Spanish.',
            'card': 'Todos Santos Plaza, Monument, Clayton and Ygnacio Valley. Two BART stations.',
            'intro': [
                'Downtown centers on Todos Santos Plaza, with a farmers market, summer concerts and restaurants. New apartments and condos have been built near the plaza and BART.',
                'The Monument Boulevard area is home to a large Latino community with Spanish-speaking businesses and services. The Clayton and Ygnacio valleys offer residential neighborhoods of single-family homes.',
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('BART', 'Concord and North Concord/Martinez'),
                ('Freeways', 'I-680, SR-4 and SR-242'),
                ('Downtown', 'Todos Santos Plaza'),
            ],
            'hoods': [
                ('Downtown & Todos Santos', 'Condos and homes near the plaza, BART and restaurants.'),
                ('Monument', 'The Monument Boulevard corridor, with a large Latino community and more affordable prices.'),
                ('Clayton Valley', 'Single-family homes on the east side, toward Clayton and Mount Diablo.'),
                ('Ygnacio Valley', 'Quiet residential neighborhoods along Ygnacio Valley Road, near Walnut Creek.'),
                ('North Concord', 'Close to North Concord/Martinez BART and Highway 4.'),
            ],
            'why': [
                ('Central location', 'I-680, Highway 4 and two BART stations.'),
                ('Price range', 'From condos to single-family homes in the valleys.'),
                ('Community', 'Spanish-speaking businesses and services, especially around Monument.'),
            ],
            'faq': [
                ('Is Concord a good fit if I work in Walnut Creek, Oakland or San Francisco?',
                 "Yes, that's why many buyers choose it: it borders Walnut Creek and Pleasant Hill, and BART takes you to Oakland and San Francisco without changing lines."),
            ],
        },
    },
    {
        'slug': 'brentwood', 'name': 'Brentwood', 'county': 'contra-costa',
        'near': ['antioch', 'pittsburg', 'concord'],
        'photo': {'file': 'brentwood.webp', 'author': 'LPS.1', 'license': 'CC0',
                  'license_url': 'https://creativecommons.org/publicdomain/zero/1.0/',
                  'source': 'https://commons.wikimedia.org/wiki/File:Downtown_Brentwood_California.jpg'},
        'es': {
            'desc': 'Realtor que habla español en Brentwood, CA. Casas más nuevas, Shadow Lakes, Trilogy y el centro en First Street. Te ayudo a comprar o vender en el este de Contra Costa.',
            'alt': 'Arco de bienvenida del centro de Brentwood, California',
            'lead': 'Brentwood ofrece casas más nuevas, espacio y un ambiente de pueblo rodeado de huertos y viñedos. Te ayudo en español a comprar o vender aquí.',
            'card': 'Casas más nuevas, Shadow Lakes y Trilogy. Ambiente de pueblo entre huertos.',
            'intro': [
                'Brentwood está en el extremo este de Contra Costa, en la planicie del Delta y con vista al Monte Diablo. Es conocida por sus granjas de frutas y verduras, muchas con U-Pick en temporada, y por su centro en First Street.',
                'Buena parte de la ciudad se construyó en las últimas décadas, así que abundan las casas más nuevas, comunidades alrededor de campos de golf como Shadow Lakes y comunidades para adultos activos como Trilogy at the Vineyards.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('Autopista', 'SR-4 (John Marsh Heritage Highway) y Vasco Road hacia Livermore'),
                ('BART más cercano', 'Antioch, con autobús express de Tri Delta Transit'),
                ('Ambiente', 'Granjas U-Pick, viñedos y golf'),
            ],
            'hoods': [
                ('Centro y First Street', 'El corazón del pueblo, con restaurantes y mercado de agricultores los sábados.'),
                ('Shadow Lakes', 'Comunidad residencial alrededor del club de golf, con casas amplias.'),
                ('Trilogy at the Vineyards', 'Comunidad para adultos activos con club deportivo, alberca y spa.'),
                ('The Streets of Brentwood', 'Zona comercial al aire libre rodeada de barrios más nuevos.'),
            ],
            'why': [
                ('Casas más nuevas', 'Mucha construcción reciente: menos reparaciones y diseños más actuales.'),
                ('Espacio y tranquilidad', 'Lotes más grandes, parques y un ritmo más calmado.'),
                ('Estilo de vida', 'Granjas, viñedos y senderos regionales a minutos de casa.'),
            ],
            'faq': [
                ('¿Cómo es el traslado desde Brentwood?',
                 'La autopista 4 conecta con Antioch y el resto del East Bay, y Vasco Road lleva hacia Livermore y la I-580. Para BART, la estación más cercana es Antioch, con autobús express de Tri Delta Transit.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Brentwood, CA. Newer homes, Shadow Lakes, Trilogy and downtown First Street. I help you buy or sell in East Contra Costa.',
            'alt': 'Welcome arch in downtown Brentwood, California',
            'lead': 'Brentwood offers newer homes, room to breathe and a small-town feel surrounded by orchards and vineyards. I help you buy or sell here, in English or Spanish.',
            'card': 'Newer homes, Shadow Lakes and Trilogy. A small-town feel among orchards.',
            'intro': [
                'Brentwood sits at the eastern edge of Contra Costa on the Delta plain, with views of Mount Diablo. It is known for its fruit and vegetable farms, many with U-Pick in season, and its downtown on First Street.',
                'Much of the city was built in recent decades, so newer homes are common, along with golf communities like Shadow Lakes and active-adult communities like Trilogy at the Vineyards.',
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('Freeway', 'SR-4 (John Marsh Heritage Highway) and Vasco Road to Livermore'),
                ('Nearest BART', 'Antioch, via Tri Delta Transit express bus'),
                ('Lifestyle', 'U-Pick farms, vineyards and golf'),
            ],
            'hoods': [
                ('Downtown & First Street', 'The heart of town, with restaurants and a Saturday farmers market.'),
                ('Shadow Lakes', 'A residential community around the golf club, with spacious homes.'),
                ('Trilogy at the Vineyards', 'An active-adult community with an athletic club, pool and spa.'),
                ('The Streets of Brentwood', 'An open-air shopping area surrounded by newer neighborhoods.'),
            ],
            'why': [
                ('Newer homes', 'Lots of recent construction: fewer repairs and more current layouts.'),
                ('Space & calm', 'Larger lots, parks and a slower pace.'),
                ('Lifestyle', 'Farms, vineyards and regional trails minutes from home.'),
            ],
            'faq': [
                ("What's the commute like from Brentwood?",
                 'Highway 4 connects to Antioch and the rest of the East Bay, and Vasco Road heads to Livermore and I-580. For BART, the closest station is Antioch, served by a Tri Delta Transit express bus.'),
            ],
        },
    },
    {
        'slug': 'richmond', 'name': 'Richmond', 'county': 'contra-costa',
        'near': ['oakland', 'san-francisco', 'concord'],
        'photo': {'file': 'richmond.webp', 'author': 'Dicklyon', 'license': 'CC BY-SA 4.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/4.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Richmond_California_aerial_(cropped).jpg'},
        'es': {
            'desc': 'Realtor que habla español en Richmond, CA. Point Richmond, Marina Bay, Hilltop y la zona de 23rd Street. BART y ferry a San Francisco. Te ayudo a comprar, vender o invertir.',
            'alt': 'Vista aérea de Richmond y su costa sobre la bahía',
            'lead': 'Richmond tiene bahía, ferry a San Francisco y barrios para distintos presupuestos, con una comunidad latina muy fuerte. Te ayudo en español a comprar, vender o invertir.',
            'card': 'Point Richmond, Marina Bay, Hilltop y 23rd Street. BART y ferry a SF.',
            'intro': [
                'Richmond, en el oeste de Contra Costa, tiene una larga costa sobre la bahía con Point Richmond, Marina Bay y el parque histórico nacional Rosie the Riveter. Cuenta con BART, Amtrak y ferry a San Francisco.',
                'Más de 4 de cada 10 residentes son latinos, y la zona de 23rd Street se ha convertido en un corredor de negocios latinos. Hay opciones desde condominios junto al agua hasta casas unifamiliares en las colinas.',
            ],
            'facts': [
                ('Condado', 'Contra Costa'),
                ('BART', 'Richmond, y El Cerrito del Norte muy cerca'),
                ('Ferry', 'Richmond–San Francisco'),
                ('Autopistas', 'I-80, I-580 y Richmond Parkway'),
            ],
            'hoods': [
                ('Point Richmond', 'El centro original de la ciudad, con ambiente de pueblo, colinas y vistas a la bahía.'),
                ('Marina Bay', 'Condominios y townhomes junto al agua, conectados al Bay Trail.'),
                ('Hilltop', 'Barrios del norte desarrollados desde los años 70, con casas más nuevas.'),
                ('23rd Street', 'Corredor de negocios latinos con casas más accesibles alrededor.'),
                ('Richmond Annex', 'Al sur, junto a El Cerrito, con casas pequeñas y bien ubicadas.'),
            ],
            'why': [
                ('Transporte', 'BART, Amtrak y ferry directo a San Francisco.'),
                ('Precio', 'Suele ser más accesible que ciudades vecinas como El Cerrito o Berkeley.'),
                ('Costa', 'Kilómetros de Bay Trail, parques y marinas.'),
            ],
            'faq': [
                ('¿Hay casas accesibles en Richmond?',
                 'Richmond suele tener precios más bajos que El Cerrito o Berkeley, pero cambian mucho de un barrio a otro. Te muestro ventas comparables reales de la zona que te interesa para que ofertes con datos.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Richmond, CA. Point Richmond, Marina Bay, Hilltop and the 23rd Street area, with BART and a ferry to San Francisco. I help you buy, sell or invest.',
            'alt': 'Aerial view of Richmond and its bay shoreline',
            'lead': 'Richmond has the bay, a ferry to San Francisco and neighborhoods for different budgets, with a strong Latino community. I help you buy, sell or invest in English or Spanish.',
            'card': 'Point Richmond, Marina Bay, Hilltop and 23rd Street. BART and a ferry to SF.',
            'intro': [
                "Richmond, in West Contra Costa, has a long bay shoreline with Point Richmond, Marina Bay and the Rosie the Riveter National Historical Park. It's served by BART, Amtrak and a ferry to San Francisco.",
                'More than 4 in 10 residents are Latino, and the 23rd Street area has become a Latino business corridor. Options range from waterfront condos to single-family homes in the hills.',
            ],
            'facts': [
                ('County', 'Contra Costa'),
                ('BART', 'Richmond, with El Cerrito del Norte close by'),
                ('Ferry', 'Richmond–San Francisco'),
                ('Freeways', 'I-80, I-580 and Richmond Parkway'),
            ],
            'hoods': [
                ('Point Richmond', "The city's original downtown, with a small-town feel, hills and bay views."),
                ('Marina Bay', 'Waterfront condos and townhomes connected to the Bay Trail.'),
                ('Hilltop', 'Northern neighborhoods developed since the 1970s, with newer homes.'),
                ('23rd Street', 'A Latino business corridor surrounded by more affordable homes.'),
                ('Richmond Annex', 'On the south side next to El Cerrito, with smaller, well-located homes.'),
            ],
            'why': [
                ('Transit', 'BART, Amtrak and a direct ferry to San Francisco.'),
                ('Price', 'Often more affordable than neighbors like El Cerrito or Berkeley.'),
                ('Shoreline', 'Miles of Bay Trail, parks and marinas.'),
            ],
            'faq': [
                ('Are there affordable homes in Richmond?',
                 "Richmond tends to be priced below El Cerrito or Berkeley, but prices vary a lot by neighborhood. I'll show you real comparable sales for the area you like so you can offer with data."),
            ],
        },
    },
    {
        'slug': 'hayward', 'name': 'Hayward', 'county': 'alameda',
        'near': ['san-leandro', 'oakland', 'san-francisco'],
        'photo': {'file': 'hayward.webp', 'author': 'Mercurywoodrose', 'license': 'CC BY-SA 3.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/3.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Hayward_City_Hall_number_3_front.jpg'},
        'es': {
            'desc': 'Realtor que habla español en Hayward, CA. Centro, Hayward Hills, Fairway Park y el sur de la ciudad. Dos estaciones de BART y el puente San Mateo. Escríbeme por WhatsApp.',
            'alt': 'Edificio del ayuntamiento de Hayward, California',
            'lead': 'Hayward está en el centro del Bay Area, con dos estaciones de BART, el puente San Mateo y una comunidad latina grande. Te ayudo en español a comprar, vender o invertir.',
            'card': 'Centro, Hayward Hills y Fairway Park. Dos BART y puente a la Península.',
            'intro': [
                'Conocida como "el corazón de la bahía", Hayward conecta con la Península por el puente San Mateo–Hayward (SR-92) y con el resto del East Bay por la I-880 y la I-580. Aquí está la universidad Cal State East Bay.',
                'Alrededor del 40% de sus residentes son latinos. Hay desde casas de posguerra en las planicies hasta casas con vista a la bahía en Hayward Hills.',
            ],
            'facts': [
                ('Condado', 'Alameda'),
                ('BART', 'Hayward (centro) y South Hayward'),
                ('Autopistas', 'I-880, I-580, SR-92 y SR-238'),
                ('Universidad', 'Cal State East Bay'),
            ],
            'hoods': [
                ('Centro', 'BART, restaurantes y nuevos condominios en un centro que se ha ido renovando.'),
                ('Hayward Hills', 'Casas en las colinas con vista a la bahía, cerca de la universidad.'),
                ('Fairway Park', 'Barrio residencial del sur, junto a Union City.'),
                ('Tennyson y el sur', 'Casas de un piso en zonas familiares, cerca del BART South Hayward.'),
            ],
            'why': [
                ('Ubicación', 'Entre Oakland, la Península y el sur de la bahía.'),
                ('Transporte', 'Dos estaciones de BART y cuatro autopistas.'),
                ('Comunidad', 'Una comunidad latina grande, con negocios y servicios en español.'),
            ],
            'faq': [
                ('¿Qué debo saber de la falla de Hayward antes de comprar?',
                 'La falla de Hayward atraviesa parte de la ciudad. Antes de ofertar revisamos la divulgación de riesgos naturales (Natural Hazard Disclosure) que el vendedor debe entregar, la inspección de la casa y el costo de un seguro contra terremotos.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in Hayward, CA. Downtown, Hayward Hills, Fairway Park and South Hayward, with two BART stations and the San Mateo Bridge. Message me on WhatsApp.',
            'alt': 'Hayward City Hall, California',
            'lead': 'Hayward sits in the middle of the Bay Area, with two BART stations, the San Mateo Bridge and a large Latino community. I help you buy, sell or invest in English or Spanish.',
            'card': 'Downtown, Hayward Hills and Fairway Park. Two BART stations and a bridge to the Peninsula.',
            'intro': [
                'Known as the "Heart of the Bay," Hayward connects to the Peninsula over the San Mateo–Hayward Bridge (SR-92) and to the rest of the East Bay via I-880 and I-580. It is home to Cal State East Bay.',
                'About 40% of residents are Latino. Homes range from post-war houses in the flatlands to bay-view homes in the Hayward Hills.',
            ],
            'facts': [
                ('County', 'Alameda'),
                ('BART', 'Hayward (downtown) and South Hayward'),
                ('Freeways', 'I-880, I-580, SR-92 and SR-238'),
                ('University', 'Cal State East Bay'),
            ],
            'hoods': [
                ('Downtown', 'BART, restaurants and new condos in a downtown that keeps improving.'),
                ('Hayward Hills', 'Hillside homes with bay views, near the university.'),
                ('Fairway Park', 'A residential neighborhood on the south side, next to Union City.'),
                ('Tennyson & South Hayward', 'Single-story homes in family neighborhoods near South Hayward BART.'),
            ],
            'why': [
                ('Location', 'Between Oakland, the Peninsula and the South Bay.'),
                ('Transit', 'Two BART stations and four freeways.'),
                ('Community', 'A large Latino community with Spanish-speaking businesses and services.'),
            ],
            'faq': [
                ('What should I know about the Hayward Fault before buying?',
                 "The Hayward Fault runs through part of the city. Before making an offer we review the seller's Natural Hazard Disclosure, the home inspection and the cost of earthquake insurance."),
            ],
        },
    },
    {
        'slug': 'san-leandro', 'name': 'San Leandro', 'county': 'alameda',
        'near': ['oakland', 'hayward', 'san-francisco'],
        'photo': {'file': 'san-leandro.webp', 'author': 'Sanfranman59', 'license': 'CC BY-SA 3.0',
                  'license_url': 'https://creativecommons.org/licenses/by-sa/3.0',
                  'source': 'https://commons.wikimedia.org/wiki/File:Casa_Peralta_(San_Leandro,_CA).JPG'},
        'es': {
            'desc': 'Realtor que habla español en San Leandro, CA. Centro, Washington Manor, la Marina y Bay Fair. Dos estaciones de BART, junto a Oakland. Te ayudo a comprar, vender o invertir.',
            'alt': 'Casa Peralta, edificio histórico de San Leandro',
            'lead': 'San Leandro, entre Oakland y Hayward, ofrece barrios tranquilos, una marina y dos estaciones de BART. Te ayudo en español a comprar, vender o invertir.',
            'card': 'Centro, Washington Manor y la Marina. Junto a Oakland, con dos BART.',
            'intro': [
                'San Leandro nació del Rancho San Leandro, otorgado a José Joaquín Estudillo en 1842, y su centro conserva edificios históricos como Casa Peralta. Hoy es una ciudad de barrios residenciales junto a Oakland.',
                'Más de una cuarta parte de sus residentes son latinos. Muchos compradores la eligen por su ubicación, con la I-880 y la I-580, dos estaciones de BART y casas unifamiliares en barrios bien establecidos.',
            ],
            'facts': [
                ('Condado', 'Alameda'),
                ('BART', 'San Leandro y Bay Fair'),
                ('Autopistas', 'I-880, I-580 e I-238'),
                ('Recreación', 'San Leandro Marina y Shoreline'),
            ],
            'hoods': [
                ('Centro', 'Sobre East 14th Street, cerca del BART San Leandro y de comercios locales.'),
                ('Washington Manor', 'Barrio familiar del oeste; algunas casas pertenecen al distrito escolar de San Lorenzo.'),
                ('La Marina', 'Junto a la bahía, con parques, senderos y el área recreativa del Shoreline.'),
                ('Bay Fair', 'En el sur, alrededor del centro comercial y el BART Bay Fair.'),
            ],
            'why': [
                ('Ubicación', 'Junto a Oakland, con acceso rápido a la I-880 y la I-580.'),
                ('BART', 'Dos estaciones: San Leandro y Bay Fair.'),
                ('Barrios establecidos', 'Casas unifamiliares en calles tranquilas.'),
            ],
            'faq': [
                ('¿A qué distrito escolar pertenece una casa en San Leandro?',
                 'La mayoría pertenece al distrito de San Leandro, pero algunas casas, sobre todo en Washington Manor, están asignadas al distrito de San Lorenzo. Lo confirmamos con la dirección exacta antes de ofertar.'),
            ],
        },
        'en': {
            'desc': 'Bilingual Realtor in San Leandro, CA. Downtown, Washington Manor, the Marina and Bay Fair, with two BART stations next to Oakland. I help you buy, sell or invest.',
            'alt': 'Casa Peralta, a historic building in San Leandro',
            'lead': 'San Leandro, between Oakland and Hayward, offers quiet neighborhoods, a marina and two BART stations. I help you buy, sell or invest in English or Spanish.',
            'card': 'Downtown, Washington Manor and the Marina. Next to Oakland, with two BART stations.',
            'intro': [
                "San Leandro grew out of Rancho San Leandro, granted to José Joaquín Estudillo in 1842, and its downtown keeps historic buildings like Casa Peralta. Today it's a city of residential neighborhoods next to Oakland.",
                'More than a quarter of residents are Latino. Many buyers choose it for its location, with I-880, I-580, two BART stations and single-family homes in established neighborhoods.',
            ],
            'facts': [
                ('County', 'Alameda'),
                ('BART', 'San Leandro and Bay Fair'),
                ('Freeways', 'I-880, I-580 and I-238'),
                ('Recreation', 'San Leandro Marina and Shoreline'),
            ],
            'hoods': [
                ('Downtown', 'Along East 14th Street, near San Leandro BART and local shops.'),
                ('Washington Manor', 'A family neighborhood on the west side; some homes are in the San Lorenzo school district.'),
                ('The Marina', 'By the bay, with parks, trails and the Shoreline recreation area.'),
                ('Bay Fair', 'On the south side, around the shopping center and Bay Fair BART.'),
            ],
            'why': [
                ('Location', 'Next to Oakland, with quick access to I-880 and I-580.'),
                ('BART', 'Two stations: San Leandro and Bay Fair.'),
                ('Established neighborhoods', 'Single-family homes on quiet streets.'),
            ],
            'faq': [
                ('Which school district does a San Leandro home belong to?',
                 "Most homes are in the San Leandro district, but some, especially in Washington Manor, are assigned to San Lorenzo. We'll confirm with the exact address before making an offer."),
            ],
        },
    },
]

# Dropdown / hub order: grouped by county.
MENU = [
    ('alameda', ['oakland', 'san-leandro', 'hayward']),
    ('contra-costa', ['richmond', 'walnut-creek', 'concord', 'pittsburg', 'antioch', 'brentwood']),
    ('san-francisco', ['san-francisco']),
]
