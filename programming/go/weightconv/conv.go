package weightconv

// KToP changes kilos to pounds
func KToP(k Kilograms) Pounds { return Pounds(k * 2.205) }

// PToK changes pounds to kilos
func PToK(p Pounds) Kilograms { return Kilograms(p / 2.205) }
