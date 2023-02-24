function FORMAT-JSON {
    [CmdletBinding(DefaultParameterSetName = 'Prettify')]
    Param(
        [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true)]
        [string]$Json,
        [Parameter(ParameterSetName = 'Minify')]
        [switch]$Minify,
        [Parameter(ParameterSetName = 'Prettify')]
        [ValidateRange(1, 1024)]
        [int]$Indentation = 4,
        [Parameter(ParameterSetName = 'Prettify')]
        [switch]$AsArray
    )
    if ($PSCmdlet.ParameterSetName -eq 'Minify') {
        return ($Json | ConvertFrom-Json) | ConvertTo-Json -Depth 100 -Compress
    }
    if ($Json -notmatch '\r?\n') {
        $Json = ($Json | ConvertFrom-Json) | ConvertTo-Json -Depth 100
    }
    $indent = 0
    $regexUnlessQuoted = '(?=([^"]*"[^"]*")*[^"]*$)'
    $result = $Json -split '\r?\n' |
    ForEach-Object {
        if ($_ -match "[}\]]$regexUnlessQuoted") {
            $indent = [Math]::Max($indent - $Indentation, 0)
        }
        $line = (' ' * $indent) + ($_.TrimStart() -replace ":\s+$regexUnlessQuoted", ': ')
        if ($_ -match "[\{\[]$regexUnlessQuoted") {
            $indent += $Indentation
        }
        $line
    }
    if ($AsArray) { return $result }
    return $result
}
 
Set-Content -Path DATABASE.jsonc -Encoding UTF8 -Value $(Get-Content -Path DATABASE.jsonc -Encoding UTF8 -Raw | ConvertFrom-Json | Sort-Object -Property QUOTE, AUTHOR -Unique | ConvertTo-Json | FORMAT-JSON)