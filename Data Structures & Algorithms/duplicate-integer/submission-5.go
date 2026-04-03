func hasDuplicate(nums []int) bool {
    // Kita buat map yang berperan sebagai Set
    set := make(map[int]struct{}) 

    for _, n := range nums {
        set[n] = struct{}{}
    }

    // Jika panjang map lebih kecil dari panjang slice, berarti ada duplikat
    return len(set) < len(nums) 
}
